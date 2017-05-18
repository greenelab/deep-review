#!/usr/bin/env python
# coding: utf-8
"""
Process citations and retrieve metadata
"""

import json
import re
import os
import pathlib
import subprocess
import textwrap

import pandas

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


# Configure directories
ref_dir = pathlib.Path('../references')
gen_dir = ref_dir.joinpath('generated')
gen_dir.mkdir(exist_ok=True)

# Read and process manuscript
text = get_text('../sections')
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


def get_standard_citatation(citation, cache):
    """
    For a citation, return (standard_citation, citation_metadata).
    Returns (None, None) if citation metadata not retrievable.
    """
    try:
        metadata = citation_to_metadata(citation, cache)
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

# Get metadata and populate standard_citation and citation_id columns
ref_df['standard_citation'], ref_df['citation_id'] = zip(
    *ref_df.citation.apply(get_standard_citatation, cache=metadata_cache))

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

dup_df = ref_df[ref_df.standard_citation.duplicated(keep=False)]
print(dup_df)

# Number of distinct references by type
type_counts = (
    ref_df
    .standard_citation
    .drop_duplicates()
    .map(lambda x: x.split(':')[0])
    .value_counts()
)
print('References by type:')
print(type_counts)

# Convert to citation_id citations for pandoc
converted_text = text
for old, new in zip(ref_df.text, ref_df.citation_id):
    old = re.escape(old)
    new = f'@{new}'
    converted_text = re.sub(old + '(?=[\s\]])', new, converted_text)
# Semicolon separate multiple refernces for pandoc-citeproc
converted_text = semicolon_separate_references(converted_text)

# Write manuscript for pandoc
with gen_dir.joinpath('all-sections.md').open('wt') as write_file:
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
with bib_path.open('wt') as write_file:
    write_file.write('\n'.join(bibtex_stanzas))

# Convert bibtex records to JSON CSL Items
bib_items = subprocess.check_output(
    ['pandoc-citeproc', '--bib2json', bib_path])
bib_items = json.loads(bib_items)
csl_items.extend(map(citeproc_passthrough, bib_items))

# Write JSON CSL bibliography for Pandoc.
with gen_dir.joinpath('bibliography.json').open('wt') as write_file:
    json.dump(csl_items, write_file, indent=2, ensure_ascii=False)
