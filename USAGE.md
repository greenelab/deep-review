# Manubot usage guidelines

This repository uses the [Manubot](https://github.com/greenelab/manubot) to automatically produce a manuscript from its source.

## Manubot markdown

Manuscript text should be written in markdown files, which should be located in [`content`](content) with a digit prefix for ordering (e.g. `01.`, `02.`, etc.) and a `.md` extension.

For basic formatting, check out the [CommonMark Help](http://commonmark.org/help/) page for an introduction to the formatting options provided by standard markdown.
In addition, manubot supports an extended version of markdown, tailored for scholarly writing, which includes [Pandoc's Markdown](http://pandoc.org/MANUAL.html#pandocs-markdown) and the extensions discussed below.

Within a paragraph in markdown, single newlines are interpreted as whitespace (same as a space).
A paragraph's source does not need to contain newlines.
However, "one paragraph per line" makes the git diff less precise, leading to less granular review commenting, and makes conflicts more likely.
Therefore, we recommend using [semantic linefeeds](http://rhodesmill.org/brandon/2012/one-sentence-per-line/ "Semantic Linefeeds. Brandon Rhodes. 2012") — newlines between sentences.
We have found that "one sentence per line" is preferable to "word wrap" or "one paragraph per line".

### Tables

Manubot supports [markdown tables](https://help.github.com/articles/organizing-information-with-tables/ "GitHub Help: Organizing information with tables").

```md
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| value_a | 1 | 47 |
| value_b | 2 | 56 |

Table: Caption for this example table. {#tbl:example-id}
```

Support for table numbering and citation is provided by [`pandoc-tablenos`](https://github.com/tomduck/pandoc-tablenos).
Above, `{#tbl:example-id}` sets the table ID, which creates an HTML anchor and allows citing the table like `@tbl:example-id`.
For easy creation of markdown tables, check out the [Tables Generator](http://www.tablesgenerator.com/markdown_tables) webapp.

### Figures

Figures can be included with the following markdown:

```md
![Caption for the example figure.](url_or_path_to_figure){#fig:example-id}
```

Support for figure numbering and citation is provided by [`pandoc-fignos`](https://github.com/tomduck/pandoc-fignos).
This figure can be cited in the text using `@fig:example-id`.
In context, a figure citation may look like: `Figure {@fig:example-id}B shows …`.

For images created by the manuscript authors that are hosted elsewhere on GitHub, we recommend using a [versioned](https://help.github.com/articles/getting-permanent-links-to-files/) GitHub URL to embed figures, thereby preserving exact image provenance.
When embedding SVG images hosted on GitHub, passing the URL through [RawGit](https://rawgit.com/) is necessary.
An example of a URL that has been passed through RawGit is:

```
https://cdn.rawgit.com/greenelab/scihub/572d6947cb958e797d1a07fdb273157ad9154273/figure/citescore.svg
```

Figures placed in the [`content/images`](content/images) directory can be embedded using their relative path.
For example, we embed an [ORCID](https://orcid.org/) icon inline using:

```md
![ORCID icon](images/orcid.svg){height="13px"}
```

The bracketed text following the image declaration is interpreted by Pandoc's [`link_attributes`](http://pandoc.org/MANUAL.html#extension-link_attributes) extension.
For example, the following will override the figure number to be "S1" and set the image width to 5 inches:

```md
{#fig:supplement tag="S1" width="5in"}
```

We recommend always specifying the width of SVG images (even if just `width="100%"`), since otherwise SVGs may not render properly in the [WeasyPrint](http://weasyprint.org/) PDF export.

### Citations

Manubot supports Pandoc [citations](http://pandoc.org/MANUAL.html#citations) via `pandoc-citeproc`.
However, Manubot performs automated citation processing and metadata retrieval on raw citations.
Therefore, citations must be of the following form: `@source:identifier`, where `source` is one of the options described below.
When choosing which source to use for a citation, we recommend the following order:

1. DOI (Digital Object Identifier), cite like `@doi:10.15363/thinklab.4`.
2. PubMed Central ID, cite like `@pmcid:PMC4497619`.
3. PubMed ID, cite like `@pmid:26158728`.
4. _arXiv_ ID, cite like `@arxiv:1508.06576v2`.
5. URL / webpage, cite like `@url:http://openreview.net/pdf?id=Sk-oDY9ge`.

Cite multiple items at once like:

```md
Here is a sentence with several citations [@doi:10.15363/thinklab.4; @pmid:26158728; @arxiv:1508.06576].
```

Note that multiple citations must be semicolon separated.
Be careful not to cite the same study using identifiers from multiple sources.
For example, the following citations all refer to the same study, but will be treated as separate references: `[@doi:10.7717/peerj.705; @pmcid:PMC4304851; @pmid:25648772]`.

#### Citation tags

The system also supports citation tags, which are recommended for the following applications:

1. A citation's identifier contains forbidden characters, such as `;` or `=`, or ends with a non-alphanumeric character other than `/`.
  In these instances, you must use a tag.
2. A single reference is cited many times.
  Therefore, it might make sense to define a tag, so if the citation updates (e.g. a newer version becomes available), only a single change is required.

Tags should be defined in [`content/citation-tags.tsv`](content/citation-tags.tsv).
If `citation-tags.tsv` defines the tag `study-x`, then this study can be cited like `@tag:study-x`.

## Reference metadata

The Manubot workflow requires the bibliographic details for references (the set of all cited works) as CSL (Citation Style Language) Items (also known as [citeproc JSON](http://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html#csl-json-items)).
The Manubot attempts to automatically retrieve metadata and generate valid citeproc JSON for references, which is exported to `output/references.json`.
However, in some cases the Manubot fails to retrieve metadata or generates incorrect or incomplete citeproc metadata.
Errors are most common for `url` references.
For these references, you can manually specify the correct citeproc in [`content/manual-references.json`](content/manual-references.json), which will override the automatically generated reference data.
To do so, create a new citeproc record that contains the field `"standard_citation"` with the appropriate reference identifier as its value.
The identifier can be obtained from the `standard_citation` column of `citations.tsv`, which is located in the `output` branch or in the `output` subdirectory of local builds.
As an example, `manual-references.json` contains:

```json
"standard_citation": "url:https://github.com/greenelab/manubot-rootstock"
```

For guidance on what CSL JSON should be like for different document types, refer to [these examples](https://github.com/aurimasv/zotero-import-export-formats/blob/a51c342e66bebd97b73a7230047b801c8f7bb690/CSL%20JSON.json).

## Manuscript metadata

[`content/metadata.yaml`](content/metadata.yaml) contains manuscript metadata that gets passed through to Pandoc, via a [`yaml_metadata_block`](http://pandoc.org/MANUAL.html#extension-yaml_metadata_block).
`metadata.yaml` should contain the manuscript `title`, `authors` list, `keywords`, and `lang` ([language tag](https://www.w3.org/International/articles/language-tags/ "W3C: Language tags in HTML and XML")).
Additional metadata, such as `date`, will automatically be created by the Manubot.
Manubot uses the [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) specified in [`build.sh`](build/build.sh) for setting the manuscript's date.
For example, setting the `TZ` environment variable to `Etc/UTC` directs the Manubot to use Coordinated Universal Time.

We recommend authors add themselves to `metadata.yaml` via pull request (when requested by a maintainer), thereby signaling that they've read and approved the manuscript.
The following YAML shows the supported key–value pairs for an author:  

```yaml
github: dhimmel  # strongly suggested
name: Daniel S. Himmelstein  # mandatory
initials: DSH  # strongly suggested
orcid: 0000-0002-3012-7446  # mandatory
twitter: dhimmel  # optional
email: daniel.himmelstein@gmail.com  # suggested
affiliations:  # as a list, strongly suggested
  - Department of Systems Pharmacology and Translational Therapeutics, University of Pennsylvania
  - Department of Biological & Medical Informatics, University of California, San Francisco
funders: GBMF4552  # optional
```

Note that `affiliations` should be a list to allow for multiple affiliations per author.

## Manubot feedback

If you experience any issues with the Manubot or would like to contribute to its source code, please visit [`greenelab/manubot`](https://github.com/greenelab/manubot) or [`greenelab/manubot-rootstock`](https://github.com/greenelab/manubot-rootstock).

## Examples

For additional examples, check out existing manuscripts that use the Manubot:

+ Satoshi Nakamoto's Bitcoin Whitepaper ([source](https://github.com/dhimmel/bitcoin-whitepaper/), [manuscript](https://dhimmel.github.io/bitcoin-whitepaper/), [commentary](https://steemit.com/manubot/@dhimmel/how-i-used-the-manubot-to-reproduce-the-bitcoin-whitepaper))
+ The Sci-Hub Coverage Study ([source](https://github.com/greenelab/scihub-manuscript), [manuscript](https://greenelab.github.io/scihub-manuscript/))
+ A Report for the Vagelos Scholars Program by Michael Zietz ([source](https://github.com/zietzm/Vagelos2017), [manuscript](https://zietzm.github.io/Vagelos2017/))
+ The Deep Review ([source](https://github.com/greenelab/deep-review), [manuscript](https://greenelab.github.io/deep-review/))
+ The Meta Review ([source](https://github.com/greenelab/meta-review), [manuscript](https://greenelab.github.io/meta-review/))
+ The Project Rephetio Manuscript ([source](https://github.com/dhimmel/rephetio-manuscript/), [manuscript](https://dhimmel.github.io/rephetio-manuscript/))
+ A Literature Review for Project Planning by David Slochower ([source](https://github.com/slochower/synthetic-motor-literature), [manuscript](https://slochower.github.io/synthetic-motor-literature/))
+ The Manubot 2018 Development Proposal ([source](https://github.com/greenelab/manufund-2018), [manuscript](https://greenelab.github.io/manufund-2018/))

If you are using the Manubot, feel free to submit a pull request to add your manuscript to the list above.
