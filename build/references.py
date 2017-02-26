
# coding: utf-8

# # Process citations and retrieve metadata

# In[1]:

import json
import re
import os
import pathlib
import subprocess

import pandas

from citations import (
    citation_to_metadata,
    citeproc_passthrough,
    get_brackets_without_reference,
    get_references_from_text,
    get_text,
    validate_reference,
)


# In[2]:

ref_dir = pathlib.Path('../references')
gen_dir = ref_dir.joinpath('generated')
gen_dir.mkdir(exist_ok=True)

# In[3]:

text = get_text('../sections')
refs = sorted(get_references_from_text(text))
warn_refs = get_brackets_without_reference(text)
if warn_refs:
    print('WARNING: The following bracketed texts are not references:')
    print('\n'.join(warn_refs))
bad_refs = list(filter(None, map(validate_reference, refs)))
if bad_refs:
    print('\n'.join(bad_refs))
    assert False
ref_df = pandas.DataFrame({'text': refs})
tag_df = pandas.read_table(ref_dir.joinpath('tags.tsv'))
tag_df['text'] = '@tag:' + tag_df.tag
ref_df = ref_df.merge(tag_df[['text', 'citation']], how='left')
ref_df.citation.fillna(ref_df.text.str.lstrip('@'), inplace=True)


# In[4]:

ref_df.head(3)


# In[5]:

def get_standard_citatation(citation, cache):
    try:
        metadata = citation_to_metadata(citation, cache)
        return metadata['standard_citation'], metadata['citation_id']
    except Exception as e:
        print(citation, e)
        return None, None


# In[6]:

cache_path = gen_dir.joinpath('citations.json')
use_cache = cache_path.exists() and 'REFRESH_METADATA_CACHE' not in os.environ
print('Using metadata cache:', use_cache)
if use_cache:
    with gen_dir.joinpath('citations.json').open() as read_file:
        metadata_cache = json.load(read_file)
else:
    metadata_cache = {}

ref_df['standard_citation'], ref_df['citation_id'] = zip(*ref_df.citation.apply(
    get_standard_citatation, cache=metadata_cache))


# In[7]:

ref_df.head(3)


# In[8]:

print(f'''
{len(ref_df)} unique citations strings extracted from text
{ref_df.standard_citation.nunique()} unique citations after standardizations
'''.strip())


# In[9]:

# Duplicated citations
dup_df = ref_df[ref_df.standard_citation.duplicated(keep=False)]
print(dup_df)

# In[10]:

converted_text = text
for old, new in zip(ref_df.text, '@' + ref_df.citation_id):
    old = re.escape(old)
    converted_text = re.sub(old + '(?=[\s\]])', new, converted_text)

with gen_dir.joinpath('all-sections.md').open('wt') as write_file:
    write_file.write(converted_text)


# In[11]:

path = gen_dir.joinpath('processed-citations.tsv')
ref_df.to_csv(path, sep='\t', index=False)

with cache_path.open('wt') as write_file:
    json.dump(metadata_cache, write_file, indent=2, ensure_ascii=False)


# In[12]:

csl_items = list()
bibtex_stanzas = list()
for metadata in metadata_cache.values():
    if 'citeproc' in metadata:
        csl_items.append(metadata['citeproc'])
    elif 'bibtex' in metadata:
        bibtex_stanzas.append(metadata['bibtex'])

bib_path = gen_dir.joinpath('bibliography.bib')
with bib_path.open('wt') as write_file:
    write_file.write('\n'.join(bibtex_stanzas))

bib_items = subprocess.check_output(['pandoc-citeproc', '--bib2json', bib_path])
bib_items = json.loads(bib_items)
csl_items.extend(map(citeproc_passthrough, bib_items))


# In[13]:

with gen_dir.joinpath('bibliography.json').open('wt') as write_file:
    json.dump(csl_items, write_file, indent=2, ensure_ascii=False)

