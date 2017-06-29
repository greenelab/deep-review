import collections
from hashlib import blake2b
import pathlib
import re

import base62
import bibtexparser

import manubot.metadata as metadata


def validate_reference(ref):
    if not ref.startswith('@'):
        return f'{ref} → does not start with @'
    source, tail = ref.lstrip('@').split(':', 1)
    if not tail:
        return f'{ref} → does not specify its source, e.g. "@doi:" or "@pmid:"'
    if source not in {'doi', 'pmid', 'arxiv', 'url', 'tag'}:
        return f'{ref} → source "{source}" is not valid'
    return None


bracketed_reference_pattern = re.compile(r'\[(@.+?)\]', flags=re.DOTALL)


def get_references_from_text(text):
    """
    Extract the set of references in a text
    """
    refs = set()
    for ref_text in bracketed_reference_pattern.findall(text):
        for ref in ref_text.split():
            if not ref:
                continue
            refs.add(ref)
    return refs


def semicolon_separate_references(text):
    """
    Separate multiple references inside the same brackets with a space and
    semicolon for pandoc-citeproc.
    """
    return bracketed_reference_pattern.sub(
        repl=lambda x: '; '.join(x.group().split()),
        string=text
    )


def get_brackets_without_reference(text):
    """
    Find bracketed text that does not start with @. Does not match
    brackets that are followed by an open parenthesis.
    """
    pattern = re.compile(r'(\[[^@][^\]]*?\])[^(]', flags=re.DOTALL)
    return list(pattern.findall(text))


def get_text(directory):
    """
    Return a dictionary of section texts in the specified directory.
    """
    section_dir = pathlib.Path(directory)
    paths = sorted(section_dir.iterdir())
    name_to_text = collections.OrderedDict()
    for path in paths:
        if not re.match(r'[0-9]', path.name):
            continue
        with path.open('rt') as section_file:
            name_to_text[path.stem] = section_file.read()
    return '\n\n'.join(name_to_text.values())


def standardize_identifier(source, identifier):
    """
    Standardize idenfiers based on their source
    """
    if source == 'doi':
        identifier = identifier.lower()
    return identifier


def citation_to_metadata(citation, cache={}, override={}):
    """
    Return a dictionary with citation metadata
    """
    source, identifer = citation.split(':', 1)
    identifer = standardize_identifier(source, identifer)
    standard_citation = f'{source}:{identifer}'
    if standard_citation not in override and standard_citation in cache:
        return cache[standard_citation]

    result = {
        'source': source,
        'identifer': identifer,
        'standard_citation': standard_citation
    }

    if standard_citation in override:
        result['citeproc'] = override[standard_citation]
    elif source == 'doi':
        result['citeproc'] = metadata.get_doi_citeproc(identifer)
        # result['bibtex'] = metadata.get_doi_bibtex(identifer)
    elif source == 'pmid':
        result['citeproc'] = metadata.get_pubmed_citeproc(identifer)
    elif source == 'arxiv':
        result['bibtex'] = metadata.get_arxiv_bibtex(identifer)
    elif source == 'url':
        result['citeproc'] = metadata.get_url_citeproc(identifer)
    else:
        msg = f'Unsupported citation  source {source} in {citation}'
        raise ValueError(msg)

    digest = blake2b(standard_citation.encode(), digest_size=6).digest()
    citation_id = base62.encodebytes(digest)
    result['citation_id'] = citation_id
    if 'citeproc' in result:
        result['citeproc'] = citeproc_passthrough(
            result['citeproc'], set_id=citation_id)
    if 'bibtex' in result:
        result['bibtex'] = bibtex_passthrough(
            result['bibtex'], set_id=citation_id)

    cache[standard_citation] = result
    return result


citeproc_type_fixer = {
    'journal-article': 'article-journal',
    'book-chapter': 'chapter',
    'posted-content': 'manuscript',
    'proceedings-article': 'paper-conference',
}

# Remove citeproc keys to fix pandoc-citeproc errors
citeproc_remove_keys = [
    # Error in $[0].ISSN[0]: failed to parse field ISSN: mempty
    'ISSN',
    # Error in $[2].ISBN[0]: failed to parse field ISBN: mempty
    'ISBN',
    # pandoc-citeproc expected Object not array for archive
    'archive',
    # failed to parse field event: Could not read as string
    'event',
    # remove the references of cited papers. Not neccessary and unwieldy.
    'reference',
]


def citeproc_passthrough(csl_item, set_id=None):
    """
    Fix errors in a CSL item and optional change its id.
    http://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html
    https://github.com/citation-style-language/schema/blob/master/csl-data.json
    """
    if set_id is not None:
        csl_item['id'] = set_id

    # Correct invalid CSL item types
    # See https://github.com/CrossRef/rest-api-doc/issues/187
    old_type = csl_item['type']
    csl_item['type'] = citeproc_type_fixer.get(old_type, old_type)

    # Remove problematic objects
    for key in citeproc_remove_keys:
        csl_item.pop(key, None)

    # pandoc-citeproc error
    # failed to parse field issued: Could not read as string: Null
    try:
        value = csl_item['issued']['date-parts'][0][0]
        if value is None:
            del csl_item['issued']
    except KeyError:
        pass

    return csl_item


def bibtex_passthrough(text, set_id=None):
    """
    Fix errors in a bibtex record and optional change its ID.
    """
    parser = bibtexparser.bparser.BibTexParser()
    parser.ignore_nonstandard_types = False
    bibdb = bibtexparser.loads(text, parser)
    entry, = bibdb.entries
    if 'author' in entry:
        entry['author'] = ' and '.join(entry['author'].rstrip(';').split('; '))
    # Set URL as url rather than link attribute
    if 'link' in entry and 'url' not in entry:
        entry['url'] = entry.pop('link')
    # Upgrade arxiv links to HTTPS
    if 'url' in entry:
        pattern = re.compile(r'^http://arxiv\.org/')
        entry['url'] = pattern.sub('https://arxiv.org/', entry['url'])
    if set_id is not None:
        entry['ID'] = set_id
    return bibtexparser.dumps(bibdb)
