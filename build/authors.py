"""
Process author table
"""

import pandas
import numpy as np

from collections import (
    defaultdict,
    OrderedDict,
)


def initials(full_name):
    """
    Return author intials in the form F.L. for First Last.  Accomodates an
    aribtrary number of whitespace-separated strings.  Converts periods to
    whitespace so that multiple middle initials are retained.
    """
    full_name = full_name.replace('.', ' ')
    name_tokens = full_name.strip().split()
    # Keeps only the first part of hyphenated names
    name_tokens = [name[0] + '.' for name in name_tokens]
    return ''.join(name_tokens)

def format_list(tokens):
    """
    Format a list of string tokens such that a pair [X, Y] is formatted 'X and
    Y' and a list [X, Y, Z] becomes 'X, Y, and Z'.  Single tokens are returned
    as-is.
    """
    if len(tokens) <= 2:
        return ' and '.join(tokens)
    else:
        tokens[-1] = 'and ' + tokens[-1]
        return ', '.join(tokens)

def get_funding(author_df):
    """
    Returns a dictionary mapping funders ('GBMF', 'NIH', 'NSF', 'OTHER') to
    award and author text.  An author may have more than one funding
    source and multiple authors may have the same funding source.
    """
    # Initially create a map from funders to dictionaries that map an award to
    # the authors supported by that award
    # funding_info data structure has the form
    # {funder1: {award1: [author1], award2: [author2, author3]}}
    funding_info = defaultdict(lambda: defaultdict(list))
    for index, row in author_df[author_df['funding'].notnull()].iterrows():
        for grant in row['funding'].split(','):
            # Separate into the funder and the award
            grant_tokens = grant.strip().split(None, 1)
            funder_map = funding_info[grant_tokens[0]]
            funder_map[grant_tokens[1]].append(row['initials'])

    formatted_info = OrderedDict()
    # Sort because the defaultdict is not ordered
    for funder in sorted(funding_info.keys()):
        # The map from awards to author lists for a single funder
        funder_map = funding_info[funder]
        funder_awards = list()
        for award in sorted(funder_map.keys()):
            authors = sorted(funder_map[award])
            funder_awards.append(f'{award} ({format_list(authors)})')
        formatted_info[funder] = format_list(funder_awards)

    return formatted_info

def get_affiliations(author_df):
    """
    Takes an author data frame in which authors have already been ordered and
    creates affiliation mappings.  Each unique affiliation is assigned an
    index based on the order in which it appears in the ordered author list.
    Complete affiliation strings are used to determine affiliation uniqueness
    even if on string contains multiple departments or institutions.
    """
    author_names = list()
    affiliations = list()
    affiliation_map = dict()
    affiliation_counter = 1

    for (_, row) in author_df.sort_values(by='static_author_order').iterrows():
        name = row['full_name']
        affiliation = row['affiliation']

        # Lookup the affiliation index or create it
        # Only list each affiliation once
        if not affiliation in affiliation_map:
            affiliation_map[affiliation] = affiliation_counter
            affiliations.append(f'{affiliation_counter}. {affiliation}')
            affiliation_counter += 1
        index = affiliation_map[affiliation]

        # Add the affiliation superscript
        # Assumes a single affiliation per author (which could contain multiple
        # institutions) but could be generalized
        # Do not add the close </sup> tag because some authors have special
        # annotations about the author ordering or correspondence
        name = f'{name}<sup>{index}'
        if pandas.notnull(row['corresponding']) and row['corresponding'].lower() == 'yes':
            name = name + ',†'
        author_names.append(name)

    # Add special annotation for the first listed author
    author_names[0] = author_names[0] + ',*'
    author_names = [name + '</sup>' for name in author_names]

    affiliation_info = OrderedDict()
    affiliation_info['authors'] = ',\n'.join(author_names)
    affiliation_info['affiliations'] = '\n'.join(affiliations)
    return affiliation_info

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

    author_info = OrderedDict()
    author_info['count'] = len(author_df)

    # Add funding, author order, and affiliation information
    author_info.update(get_funding(author_df))
    author_info.update(get_affiliations(author_df))

    return author_info
