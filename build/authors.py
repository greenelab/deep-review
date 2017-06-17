"""
Process author table
"""

import pandas


def get_author_info(author_file):
    """
    Load the author table and return a dict with author information such as
    the number of authors.
    """
    author_df = pandas.read_table(author_file)

    author_info = dict()
    author_info['count'] = len(author_df)
    return author_info
