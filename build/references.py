#!/usr/bin/env python
# coding: utf-8
"""
Process citations and retrieve citation metadata
"""

import collections
import json
import os
import pathlib
import re
import subprocess
import textwrap

import jinja2
import pandas
import yaml

from citations import (
    citation_to_metadata,
    citeproc_passthrough,
    get_brackets_without_reference,
    get_references_from_text,
    get_text,
    semicolon_separate_references,
    validate_reference,
)

# Run only as a script
assert __name__ == '__main__'


def get_divider(title='Error', linewidth=79, fill_character='#'):
    """
    Useful for separating sections in logs
    """
    lines = [
        '',
        fill_character * linewidth,
        f' {title} '.center(linewidth, fill_character),
    ]
    return '\n'.join(lines)


def get_pandoc_metadata(path):
    """
    Load all of the metadata from a yaml file, & return.

    :param path: pathlib.Path to a metadata YAML file.
    :return: structured metadata object.
    """
    with path.open('r') as read_file:
        metadata_dict = yaml.load(read_file)
    metadata_dict['author'] = []
    # Reformat author to match ``yaml_metadata_block`` formatting
    for author in metadata_dict['author_info']:
        if 'full_name' in author.keys():
            metadata_dict['author'].append(author['full_name'])
    return metadata_dict


def get_author_info(path):
    """
    Load the author table and return the list of authors.

    :param path: pathlib.Path to a metadata YAML file.
    :return: dict with structured author metadata.
    """
    # Detect issues with author information
    metadata_dict = get_pandoc_metadata(path)['author_info']
    format_issues_dict = {'missing': {'initials': []},
                     'duplicate': {'initials': [], 'full_name': []} }
    format_check_failed = False
    for author_index, author in enumerate(metadata_dict):
        for key, key_absences in format_issues_dict['missing'].items():
            if key not in author.keys():
                key_absences.append(author_index)
                format_check_failed = True
        for key, key_occurences in format_issues_dict['duplicate'].items():
            if key in author and author[key] in key_occurences:
                key_occurences[author[key]].append(author_index)
                format_check_failed = True

    # Print descriptive message for invalid author information
    if format_check_failed is True:
        msg = ''
        for format_issue, format_issue_sub_dict in format_issues_dict.items():
            for key, blame_list in format_issue_sub_dict.items():
                msg += f'{format_issue} {key} detected in metadata.yaml for author(s): {blame_list}\n'.replace('_', ' ').capitalize()
        raise ValueError(msg)
    return metadata_dict


# Manuscript statistics
stats = collections.OrderedDict()

# Configure directories
ref_dir = pathlib.Path('../references')
gen_dir = ref_dir.joinpath('generated')
gen_dir.mkdir(exist_ok=True)

# Read and process manuscript
text = get_text('../content')
refs = sorted(get_references_from_text(text))

# Warn about non-failing misformatted references
warn_refs = get_brackets_without_reference(text)
if warn_refs:
    print(get_divider('References Warning'))
    print('Potentially misformatted references detected:')
    print('\n'.join(warn_refs))

# Failing references
bad_refs = list(filter(None, map(validate_reference, refs)))
if bad_refs:
    print(get_divider('References Error'))
    print('Misformatted references detected:')
    print('\n'.join(bad_refs))
    raise SystemExit(1)


ref_df = pandas.DataFrame({'text': refs})
tag_df = pandas.read_table(ref_dir.joinpath('tags.tsv'))
tag_df['text'] = '@tag:' + tag_df.tag
ref_df = ref_df.merge(tag_df[['text', 'citation']], how='left')
ref_df.citation.fillna(ref_df.text.str.lstrip('@'), inplace=True)


def get_standard_citatation(citation, cache, override):
    """
    For a citation, return (standard_citation, citation_metadata).
    Returns (None, None) if citation metadata not retrievable.
    """
    try:
        metadata = citation_to_metadata(citation, cache, override)
        return metadata['standard_citation'], metadata['citation_id']
    except Exception as e:
        return None, None


# Load metadata cache
cache_path = gen_dir.joinpath('citations.json')
use_cache = cache_path.exists() and 'REFRESH_METADATA_CACHE' not in os.environ
print('Using metadata cache:', use_cache)
if use_cache:
    with gen_dir.joinpath('citations.json').open() as read_file:
        metadata_cache = json.load(read_file)
else:
    metadata_cache = {}

# Read manual citations (overrides)
with ref_dir.joinpath('manual-references.json').open() as read_file:
    overrides = json.load(read_file)
overrides = {ref.pop('standard_citation'): ref for ref in overrides}

# Get metadata and populate standard_citation and citation_id columns
result = ref_df.citation.apply(
    get_standard_citatation, cache=metadata_cache, override=overrides)
ref_df['standard_citation'], ref_df['citation_id'] = zip(*result)

broken_citations = ref_df[ref_df.citation_id.isnull()]
if not broken_citations.empty:
    bad = '\n'.join(broken_citations['text'])
    message = get_divider('References Error') + textwrap.dedent('''
    Metadata could not be retrieved for the following citations:
    {}
    ''').format(bad)
    raise SystemExit(message)

# Check that no two standard_citations have the same citation_id
# which could occur due to a hash collision
collision_df = ref_df[['standard_citation', 'citation_id']].drop_duplicates()
collision_df = collision_df[collision_df.citation_id.duplicated(keep=False)]
if not collision_df.empty:
    print(collision_df)
    raise SystemExit(f'OMF! Hash collision. Congratulations.')

# Duplicated citations
print(f'''
{len(ref_df)} unique citations strings extracted from text
{ref_df.standard_citation.nunique()} unique citations after standardizations
'''.strip())

print(
    ref_df[ref_df.standard_citation.duplicated(keep=False)]
    .sort_values('standard_citation')
    .to_string(index=False, columns=['standard_citation', 'text'])
)

# Number of distinct references by type
ref_counts = (
    ref_df
    .standard_citation
    .drop_duplicates()
    .map(lambda x: x.split(':')[0])
    .pipe(collections.Counter)
)
ref_counts['total'] = sum(ref_counts.values())
stats['reference_counts'] = ref_counts
print('References by type:')
print(ref_counts)

# Author table information
authors_path = pathlib.Path('../content/metadata.yml')
stats['authors'] = get_author_info(authors_path)

with gen_dir.joinpath('stats.json').open('wt') as write_file:
    json.dump(stats, write_file, indent=2)

# Convert to citation_id citations for pandoc
converted_text = text
for old, new in zip(ref_df.text, ref_df.citation_id):
    old = re.escape(old)
    new = f'@{new}'
    converted_text = re.sub(old + '(?=[\s\]])', new, converted_text)
# Semicolon separate multiple refernces for pandoc-citeproc
converted_text = semicolon_separate_references(converted_text)

# Template using jinja2
jinja_environment = jinja2.Environment(
    loader=jinja2.BaseLoader(),
    comment_start_string='{##',
)
template = jinja_environment.from_string(converted_text)
converted_text = template.render(**stats)

# Fetch metadata
pandoc_metadata_dict = get_pandoc_metadata(pathlib.Path('../content/metadata.yml'))

# Write manuscript for pandoc
all_sections_path = gen_dir.joinpath('all-sections.md')
with all_sections_path.open('wt') as write_file:
    yaml.dump(pandoc_metadata_dict, write_file, explicit_start=True,
              explicit_end=True, default_flow_style=False)
    write_file.write(converted_text)

# Write citation table
path = gen_dir.joinpath('processed-citations.tsv')
ref_df.to_csv(path, sep='\t', index=False)

# Write metadata cache
with cache_path.open('wt') as write_file:
    json.dump(metadata_cache, write_file, indent=2, ensure_ascii=False)


# Generate CSL items for Pandoc
csl_items = list()
bibtex_stanzas = list()
for metadata in metadata_cache.values():
    if 'citeproc' in metadata:
        csl_items.append(metadata['citeproc'])
    elif 'bibtex' in metadata:
        bibtex_stanzas.append(metadata['bibtex'])

# Write bibtex bibliography
bib_path = gen_dir.joinpath('bibliography.bib')
bib_path.write_text('\n'.join(bibtex_stanzas))

# Convert bibtex records to JSON CSL Items
bib_items = subprocess.check_output(
    ['pandoc-citeproc', '--bib2json', bib_path])
bib_items = json.loads(bib_items)
csl_items.extend(map(citeproc_passthrough, bib_items))

# Write JSON CSL bibliography for Pandoc.
with gen_dir.joinpath('bibliography.json').open('wt') as write_file:
    json.dump(csl_items, write_file, indent=2, ensure_ascii=False)
