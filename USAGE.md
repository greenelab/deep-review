# Manubot usage guidelines

This repository uses [Manubot](https://manubot.org) to automatically produce a manuscript from the source in the [`content`](content) directory.
Check out the [Manubot catalog](https://manubot.org/catalog/) for examples of what is possible when writing with Manubot.
Try editing the [demo manuscript](https://github.com/manubot/try-manubot) to quickly test Manubot formatting and citations.

## Manubot markdown

Manuscript text should be written in markdown files located in the [`content`](content) directory.
Markdown files are identified by their `.md` extension and ordered according to their two-digit prefix (e.g. `01.`, `02.`, … `99.`).

For basic formatting, check out the [CommonMark Help](https://commonmark.org/help/) page for an introduction to the formatting options provided by standard markdown.
In addition, Manubot supports an extended version of markdown, tailored for scholarly writing, which includes [Pandoc's Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown) and the extensions discussed below.

The `content/02.delete-me.md` file in the Rootstock repository shows many of the elements and formatting options supported by Manubot.
See the [raw markdown](https://gitlab.com/manubot/rootstock/blob/master/content/02.delete-me.md#L) in this file and compare it to the [rendered manuscript](https://manubot.github.io/rootstock/).

Within a paragraph in markdown, single newlines are interpreted as whitespace (same as a space).
A paragraph's source does not need to contain newlines.
However, "one paragraph per line" makes the git diff less precise, leading to less granular review commenting, and makes conflicts more likely.
Therefore, we recommend using [semantic linefeeds](https://rhodesmill.org/brandon/2012/one-sentence-per-line/ "Semantic Linefeeds. Brandon Rhodes. 2012") — newlines between sentences.
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
For easy creation of markdown tables, check out the [Tables Generator](https://www.tablesgenerator.com/markdown_tables) webapp.

### Figures

Figures can be included with the following markdown:

```md
![Caption for the example figure.](url_or_path_to_figure){#fig:example-id}
```

Support for figure numbering and citation is provided by [`pandoc-fignos`](https://github.com/tomduck/pandoc-fignos).
This figure can be cited in the text using `@fig:example-id`.
In context, a figure citation may look like: `Figure {@fig:example-id}B shows …`.

For images created by the manuscript authors that are hosted elsewhere on GitHub, we recommend using a [versioned](https://help.github.com/articles/getting-permanent-links-to-files/) GitHub URL to embed figures, thereby preserving exact image provenance.
When embedding SVG images hosted on GitHub, it's necessary to append `?sanitize=true` to the `raw.githubusercontent.com` URL.
For example:

```
https://raw.githubusercontent.com/greenelab/scihub/572d6947cb958e797d1a07fdb273157ad9154273/figure/citescore.svg?sanitize=true
```

Figures placed in the [`content/images`](content/images) directory can be embedded using their relative path.
For example, we embed an [ORCID](https://orcid.org/) icon inline using:

```md
![ORCID icon](images/orcid.svg){height="13px"}
```

The bracketed text following the image declaration is interpreted by Pandoc's [`link_attributes`](https://pandoc.org/MANUAL.html#extension-link_attributes) extension.
For example, the following will override the figure number to be "S1" and set the image width to 5 inches:

```md
{#fig:supplement tag="S1" width="5in"}
```

We recommend always specifying the width of SVG images (even if just `width="100%"`), since otherwise SVGs may not render properly in the [WeasyPrint](https://weasyprint.org/) PDF export.

### Citations

Manubot supports Pandoc [citations](https://pandoc.org/MANUAL.html#citations) via `pandoc-citeproc`.
However, Manubot performs automated citation processing and metadata retrieval on in-text citations.
Therefore, citations must be of the following form: `@source:identifier`, where `source` is one of the options described below.
When choosing which source to use for a citation, we recommend the following order:

1. DOI (Digital Object Identifier), cite like `@doi:10.15363/thinklab.4`.
   Shortened versions of DOIs can be created at [shortdoi.org](http://shortdoi.org/).
   shortDOIs begin with `10/` rather than `10.` and can also be cited.
   For example, Manubot will expand `@doi:10/993` to the DOI above.
   We suggest using shortDOIs to cite DOIs containing forbidden characters, such as `(` or `)`.
2. PubMed Central ID, cite like `@pmcid:PMC4497619`.
3. PubMed ID, cite like `@pmid:26158728`.
4. _arXiv_ ID, cite like `@arxiv:1508.06576v2`.
5. ISBN (International Standard Book Number), cite like `@isbn:9781339919881`.
6. URL / webpage, cite like `@url:https://nyti.ms/1QUgAt1`.
   URL citations can be helpful if the above methods return incorrect metadata.
   For example, `@doi:10.1038/ng.3834` [incorrectly handles](https://github.com/manubot/manubot/issues/158) the consortium name resulting in a blank author, while `@url:https://doi.org/10.1038/ng.3834` succeeds.
   Similarly, `@url:https://doi.org/10.1101/142760` is a [workaround](https://github.com/manubot/manubot/issues/16) to set the journal name of bioRxiv preprints to _bioRxiv_.
7. Wikidata Items, cite like `@wikidata:Q50051684`.
   Note that anyone can edit or add records on [Wikidata](https://www.wikidata.org), so users are encouraged to contribute metadata for hard-to-cite works to Wikidata as an alternative to using a `raw` citation.
8. For references that do not have any of the persistent identifiers above, use a raw citation like `@raw:old-manuscript`.
   Metadata for raw citations must be provided manually.

Cite multiple items at once like:

```md
Here is a sentence with several citations [@doi:10.15363/thinklab.4; @pmid:26158728; @arxiv:1508.06576; @isbn:9780394603988].
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

Manubot stores the bibliographic details for references (the set of all cited works) as CSL JSON ([Citation Style Language Items](http://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html#csl-json-items)).
For all citation sources besides `raw`, Manubot automatically generates CSL JSON.
In some cases, automatic metadata retrieval fails or provides incorrect or incomplete information.
Errors are most common for `url` references.
Therefore, Manubot supports user-provided metadata, which we refer to as "manual references".
When a manual reference is provided, Manubot uses the supplied metadata and does not attempt to generate it.

Manubot searches the `content` directory for files that match the glob pattern `manual-references*.*` and expects that these files contain manual references.
[`content/manual-references.json`](content/manual-references.json) is the default file to specify custom CSL JSON metadata.
Manual references are matched to citations using their "id" field.
For example, to manually specify the metadata for the citation `@url:https://github.com/manubot/rootstock`, add a CSL JSON Item to `manual-references.json` that contains the following excerpt:

```json
"id": "url:https://github.com/manubot/rootstock",
```

The metadata for `raw` citations must be provided in a manual reference file (e.g. `manual-references.json`) or an error will occur.
For example, to cite `@raw:private-message` in a manuscript, a corresponding CSL JSON Item is required, such as:

```json
{
  "id": "raw:private-message",
  "type": "personal_communication",
  "title": "Personal communication with Doctor X"
}
```

All manual references must provide values for the "id" and "type" fields.
For guidance on what CSL JSON should be like for different document types, refer to [these examples](https://github.com/aurimasv/zotero-import-export-formats/blob/a51c342e66bebd97b73a7230047b801c8f7bb690/CSL%20JSON.json).

Manubot offers some support for other bibliographic metadata formats besides CSL JSON, by delegating conversion to the `pandoc-citeproc --bib2json` [utility](https://github.com/jgm/pandoc-citeproc/blob/master/man/pandoc-citeproc.1.md#convert-mode).
Formats are inferred from filename extensions.
So, for example, to provide metadata for `@url:https://github.com/manubot/rootstock` in BibTeX format, create the file `content/manual-references.bib` and create an item whose definition starts with the excerpt:

```latex
@misc{url:https://github.com/manubot/rootstock,
```

Processed reference metadata in CSL JSON format, either generated by Manubot or specified via manual references, is exported to `references.json`.
This file is located in the `output` branch on GitHub or in the `output` subdirectory of local builds.
The "id" field in `references.json` and in the final manuscript uses a shortened ID that is derived from the original ID.
For debugging information, see `citations.tsv`, which shows citation identifiers as they progress through the processing pipeline.
In order to freeze all references, rather than have Manubot regenerate them during future builds, copy the `references.json` output file to `content` with a filename matching the `manual-references*.json` pattern.
One tip is to embed the date `references.json` was generated into the frozen manual reference filename, like `content/manual-references-2019-06-21.json`.

## Manuscript metadata

[`content/metadata.yaml`](content/metadata.yaml) contains manuscript metadata that gets passed through to Pandoc, via a [`yaml_metadata_block`](https://pandoc.org/MANUAL.html#extension-yaml_metadata_block).
`metadata.yaml` should contain the manuscript `title`, `authors` list, `keywords`, and `lang` ([language tag](https://www.w3.org/International/articles/language-tags/ "W3C: Language tags in HTML and XML")).
Additional metadata, such as `date`, will automatically be created by the Manubot.
Manubot uses the [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) specified in [`build.sh`](build/build.sh) for setting the manuscript's date.
For example, setting the `TZ` environment variable to `Etc/UTC` directs the Manubot to use Coordinated Universal Time.

We recommend authors add themselves to `metadata.yaml` via pull request (when requested by a maintainer), thereby signaling that they've read and approved the manuscript.
The following YAML shows the supported key–value pairs for an author:  

```yaml
github: dhimmel  # strongly suggested
name: Daniel S. Himmelstein  # mandatory
initials: DSH  # optional
orcid: 0000-0002-3012-7446  # mandatory
twitter: dhimmel  # optional
email: daniel.himmelstein@gmail.com  # suggested
affiliations:  # as a list, strongly suggested
  - Department of Systems Pharmacology and Translational Therapeutics, University of Pennsylvania
  - Department of Biological & Medical Informatics, University of California, San Francisco
funders: GBMF4552  # optional
```

Note that `affiliations` should be a list to allow for multiple affiliations per author.

### Thumbnail

A thumbnail is an image used to visually represent the manuscript,
such as when a manuscript is shared on social media or added to the [Manubot catalog](https://manubot.org/catalog/).
Specify a thumbnail in any of the following ways:

1. placing an image named `thumbnail.png` anywhere in the manuscript repository (for example, in the root directory).
2. setting `thumbnail` in `metadata.yaml` to a path, relative to the repository root, where the image file is located.
    Example:
    ```yaml
    thumbnail: build/assets/thumbnail-1000x1000.png
    ```
3. setting `thumbnail` in `metadata.yaml` to an absolute URL where the image is located.
    Example:
    ```yaml
    thumbnail: https://github.com/greenelab/meta-review/raw/master/thumbnail.png
    ```

Methods 2 and 3 take precedence over method 1.
View the [guidelines here](https://github.com/manubot/catalog#thumbnail-guidelines) for suggestions on how to create a good thumbnail.
Key points are that thumbnails should be 1000 × 1000 pixels, PNG formatted, and striking.

## Custom formatting

Modifying the manuscript formatting requires modifying the CSS in the file [`build/themes/default.html`](build/themes/default.html).
Common formatting changes, such as [font size](https://github.com/manubot/rootstock/issues/239) and [double spacing](https://github.com/manubot/rootstock/issues/244), can be found by searching the [Rootstock issues](https://github.com/manubot/rootstock/issues).
Open a [new issue](https://github.com/manubot/rootstock/issues/new) if you have a new formatting question.

Changing the citation style or which interactive HTML plugins are loaded requires editing the build script [`build/build.sh`](build/build.sh).
The citation style is determined by the Citation Style Language file specified by `CSL_PATH`.
It can be changed to use other existing styles as [described here](https://github.com/manubot/rootstock/issues/242#issuecomment-507688339).

## Manubot feedback

If you experience any issues with the Manubot or would like to contribute to its source code, please visit [`manubot/manubot`](https://github.com/manubot/manubot) or [`manubot/rootstock`](https://github.com/manubot/rootstock).

## Citing Manubot

To cite the Manubot project or for more information on its design and history, see `@doi:10.1371/journal.pcbi.1007128`:

> **Open collaborative writing with Manubot**<br>
Daniel S. Himmelstein, Vincent Rubinetti, David R. Slochower, Dongbo Hu, Venkat S. Malladi, Casey S. Greene, Anthony Gitter<br>
*PLOS Computational Biology* (2019-06-24) <https://doi.org/c7np><br>
DOI: [10.1371/journal.pcbi.1007128](https://doi.org/10.1371/journal.pcbi.1007128) · PMID: [31233491](https://www.ncbi.nlm.nih.gov/pubmed/31233491)

The Manubot version of this manuscript is available at <https://greenelab.github.io/meta-review/>.

## Acknowledgments

We would like to thank the contributors and funders whose support makes the Manubot project possible.
Specifically, Manubot development has been financially supported by:

- the **Alfred P. Sloan Foundation** in [Grant G-2018-11163](https://sloan.org/grant-detail/8501) to [**@dhimmel**](https://github.com/dhimmel).
- the **Gordon & Betty Moore Foundation** ([**@DDD-Moore**](https://github.com/DDD-Moore)) in [Grant GBMF4552](https://www.moore.org/grant-detail?grantId=GBMF4552) to [**@cgreene**](https://github.com/cgreene).
