"""
Process author table
"""

import collections
import pandas
import numpy as np


def initials(full_name):
    """
    Return author intials in the form F.L. for First Last.  Accomodates an
    aribtrary number of whitespace-separated strings.
    """
    name_tokens = full_name.strip().split()
    # Keeps only the first part of hyphenated names
    name_tokens = [name[0] + '.' for name in name_tokens]
    return ''.join(name_tokens)

def get_author_info(author_file):
    """
    Load the author table and return a dict with author information such as
    the number of authors.
    """
    author_df = pandas.read_table(author_file)

    # Add author initials
    author_df['initials'] = author_df['full_name'].apply(initials)

    # Avoid initial collisions, will need a more general way to refer to
    # authors if they occur
    assert len(author_df['initials'].unique()) == len(author_df), \
        'All authors must have unique initials'
    assert np.all(author_df['approve'].str.match('Yes', case=False)), \
        'All contributors must approve of the manuscript before being ' + \
        'added as authors'

    author_info = collections.OrderedDict()
    author_info['count'] = len(author_df)
    return author_info
