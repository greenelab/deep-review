import json
import re
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
    citeproc = response.json()
    # Upgrade to preferred formatting in DOI resolution URLs
    if 'URL' in citeproc:
        pattern = re.compile(r'^(https?://d?x?\.?)doi\.org/')
        citeproc['URL'] = pattern.sub('https://doi.org/', citeproc['URL'])
    return citeproc


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
    citeproc = response.json()
    citeproc['URL'] = f'https://www.ncbi.nlm.nih.gov/pubmed/{pubmed_id}'
    return citeproc


def get_url_citeproc_greycite(url):
    """
    Uses Greycite which has experiened uptime problems in the past.
    API calls seem to take at least 15 seconds. Browser requests are much
    faster. Setting header did not have an effect. Consider mimicking browser
    using selenium.

    More information on Greycite at:
    http://greycite.knowledgeblog.org/
    http://knowledgeblog.org/greycite
    https://arxiv.org/abs/1304.7151
    https://git.io/v9N2C

    Uses urllib.request.urlopen rather than requests.get due to
    https://github.com/kennethreitz/requests/issues/4023
    """
    response = requests.get(
        'http://greycite.knowledgeblog.org/json',
        params={'uri': url},
        headers={'Connection': 'close'},
    )
    # Some Greycite responses were valid JSON besides for an error appended
    # like "<p>*** Date set from uri<p>" or "<p>*** fetch error : 404<p>".
    pattern = re.compile(r"<p>\*\*\*.*<p>")
    text = pattern.sub('', response.text)
    csl_item = json.loads(text)
    csl_item['type'] = 'webpage'
    return csl_item


def get_url_citeproc_manual(url):
    """
    Manually create citeproc for a URL.
    """
    return {
        'URL': url,
        'type': 'webpage',
    }


def get_url_citeproc(url):
    """
    Get citeproc for a URL trying a sequence of strategies.
    """
    try:
        return get_url_citeproc_greycite(url)
    except Exception as e:
        print(f'Error getting {url} from Greycite: {e}')
        # Fallback strategy
        return get_url_citeproc_manual(url)


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
