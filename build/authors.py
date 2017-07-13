"""
Process author table
"""

import pandas


def get_author_info(path):
    """
    Load the author table and return the list of authors.
    """
    author_df = pandas.read_table(path)

    # Detect missing full name
    missing_full_name = author_df[author_df['full_name'].isnull()].index.tolist()
    if missing_full_name:
        msg = f'Missing full name in authors.tsv for author(s): {missing_full_name}'
        raise ValueError(msg)

    # Detect missing author initials
    missing_initials = author_df[author_df['initials'].isnull()].index.tolist()
    if missing_initials:
        msg = f'Missing initials in authors.tsv for author(s): {missing_initials}'
        raise ValueError(msg)

    # Detect duplicate author initials
    duplicated_initials = list(
        author_df[author_df.duplicated('initials')].initials)
    if duplicated_initials:
        msg = f'Duplicated initials in authors.tsv: {duplicated_initials}'
        raise ValueError(msg)

    # Replace missing values with None
    author_df.where(pandas.notnull(author_df), None, inplace=True)

    authors = author_df.to_dict(orient='records')
    return authors
