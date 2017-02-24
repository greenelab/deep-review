import urllib.request

import requests


def get_short_doi(doi, cache={}, verbose=False):
    """
    Get the shortDOI for a DOI. Providing a cache dictionary will prevent
    multiple API requests for the same DOI.
    """
    if doi in cache:
        return cache[doi]
    quoted_doi = urllib.request.quote(doi)
    url = 'http://shortdoi.org/{}?format=json'.format(quoted_doi)
    try:
        response = requests.get(url).json()
        short_doi = response['ShortDOI']
    except Exception as e:
        if verbose:
            print(doi, 'failed with', e)
        return None
    cache[doi] = short_doi
    return short_doi


def get_doi_citeproc(doi):
    """
    Use Content Negotioation (http://citation.crosscite.org/docs.html) to
    retrieve the citeproc JSON citation for a DOI.
    """
    url = 'https://doi.org/' + urllib.request.quote(doi)
    header = {
        'Accept': 'application/vnd.citationstyles.csl+json',
    }
    response = requests.get(url, headers=header)
    return response.json()


def get_pubmed_citeproc(pubmed_id):
    """
    Get the citeproc JSON for a PubMed or PubMed Central identifier

    https://github.com/ncbi/citation-exporter
    https://www.ncbi.nlm.nih.gov/pmc/tools/ctxp/
    https://www.ncbi.nlm.nih.gov/pmc/utils/ctxp/samples
    """
    params = {
        'ids': pubmed_id,
        'report': 'citeproc'
    }
    url = 'https://www.ncbi.nlm.nih.gov/pmc/utils/ctxp'
    response = requests.get(url, params)
    return response.json()


# def get_url_citeproc(url):
#     """
#     Uses greycite (unreliable)
#     https://github.com/cboettig/knitcitations/blob/master/R/greycite.R
#     """
#     params = {'uri': url}
#     url = 'http://greycite.knowledgeblog.org/'
#     response = requests.get(url, params)
#     print(response.url)
#     return response


def get_url_citeproc(url):
    """
    Uses greycite (unreliable)
    https://github.com/cboettig/knitcitations/blob/master/R/greycite.R
    """
    return {
        'URL': url,
        'type': 'webpage'
    }


def get_doi_bibtex(doi):
    """
    Use DOI Content Negotioation (http://crosscite.org/cn/) to retrieve a
    string with the bibtex entry.
    """
    url = 'https://doi.org/' + urllib.request.quote(doi)
    header = {
        'Accept': 'application/x-bibtex',
    }
    response = requests.get(url, headers=header)
    bibtext = response.text
    return bibtext


def get_arxiv_bibtex(arxiv_id):
    """
    Use the arxiv2bib package to get the BibTex for an arXiv preprint.
    """
    import arxiv2bib
    ref, = arxiv2bib.arxiv2bib([arxiv_id])
    if isinstance(ref, arxiv2bib.ReferenceErrorInfo):
        raise KeyError(f'{ref.message}: {arxiv_id}')
    return ref.bibtex()
