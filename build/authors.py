"""
Process author table
"""

import pandas


def get_author_info(path):
    """
    Load the author table and return the list of authors.
    """
    author_df = pandas.read_table(path)

    # Detect duplicate author initials
    duplicated_initials = list(
        author_df[author_df.duplicated('initials')].initials)
    if duplicated_initials:
        msg = f'Duplicated initials in authors.tsv: {duplicated_initials}'
        raise ValueError(msg)

    authors = author_df.to_dict(orient='records')
    return authors
