import collections
import pathlib
import re


def get_references_from_text(text):
    """
    Extract the set of references in a text
    """
    refs = set()
    for ref_text in re.findall(r'\[(@.+?)\]', text):
        for ref in ref_text.split(' '):
            ref = ref.lstrip('@')
            refs.add(ref)
    return refs


def get_texts(directory):
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
    return name_to_text


if __name__ == '__main__':
    """
    Print the sorted list of all extracted references
    """
    sections = get_texts('../sections')
    refs = set()
    for section in sections.values():
        refs |= get_references_from_text(section)
    print('\n'.join(sorted(refs)))
