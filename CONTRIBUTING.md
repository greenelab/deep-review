# Manuscript contribution guidelines

## Markdown

The paper will be written using markdown. Markdown files use the `.md` extension.
Check out the [CommonMark Help](http://commonmark.org/help/) page for an introduction to formatting options provided by markdown.
In addition, to standard markdown features, we support [markdown tables](https://help.github.com/articles/organizing-information-with-tables/ "GitHub Help: Organizing information with tables") and a custom citation syntax.
Check out [Tables Generator](http://www.tablesgenerator.com/markdown_tables) for creating markdown tables.

The custom citation guidelines are as follows:

1. Always use a DOI for the version of record if available.
  Cite DOIs like `[@doi:10.15363/thinklab.4]`.
2. If the version of record doesn't have a DOI but does have a PubMed ID, cite like `[@pmid:26158728]`.
3. If the article is an _arXiv_ preprint, cite like `[@arxiv:1508.06576]`.
4. If and only if the article has none of the above, cite with the URL like `[@url:http://openreview.net/pdf?id=Sk-oDY9ge]`.

You cite multiple items at once like `[@doi:10.15363/thinklab.4 @pmid:26158728 @arxiv:1508.06576]`.

The system also supports tags, which may be helpful when a single reference is cited many times.
For example, you can add a reference to the tag `study_x` using the following syntax: `[@tag:study_x]`.
If you add references that use tags, make sure to add those tags and their corresponding citations to [`references/tags.tsv`](references/tags.tsv).

If the automatically extracted reference information contains errors, it can be [manually overridden](references/README.md#reference-overrides).

## Authorship information

Authorship information and order is extracted from [`authors.tsv`](../content/authors.tsv).
To add an author, insert a row into this table.
We recommend authors add themselves to `authors.tsv` via pull request (when requested by a maintainer), thereby signaling that they've read and approved the manuscript.
