# Contribution guidelines for the deep-review repository

## Issues

We'll use issues for discussion of papers, section outlines, and other
structural components of the paper.

## Pull requests

Contributions to the article operate on a pull request model. We expect
participants to actively review pull requests. We'd love to have you ask
questions, clarify points, and jump in and edit the text.

## Authorship

What qualifies as authorship? We use the [ICJME Guidelines](http://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html).
We expect authors to contribute to the overall design by participating in
issues, to contribute to the text by contributing sections and/or revisions
to sections through pull requests. It is important to note that, for authorship,
these should be substantial intellectual contributions.

## Peer review

All pull requests will undergo peer review. Participants in this project should
review the changes. They should suggest modifications or, potentially, directly
edit the pull request to make suggested changes. Reviewers can note approval by
commenting ":+1:", "looks good to me", or "approved". As a reviewer, it's
helpful to note the type of review you performed: did you read cited literature,
look over the text in detail, or are you just supporting the concept?

Before a repository maintainer merges a pull request, there must be at least
one affirmative review. If there is any unaddressed criticism or disapproval,
a repository maintainer will determine how to proceed and may wait for
additional feedback.

## Markdown

The paper will be written using markdown. Markdown files use the `.md`
extension. Check out the [CommarkMark Help](http://commonmark.org/help/) page
for an introduction to formatting options provided by markdown. In addition, to
standard markdown features, we support [markdown
tables](https://help.github.com/articles/organizing-information-with-tables/
"GitHub Help: Organizing information with tables") and a custom citation syntax.
Check out [Tables Generator](http://www.tablesgenerator.com/markdown_tables) for
creating markdown tables.

The custom citation guidelines are as follows:

1. Always use a DOI for the version of record if available. Cite DOIs like
  `[@doi:10.15363/thinklab.4]`.
+ If the version of record doesn't have a DOI but does have a PubMed ID, cite
  like `[@pmid:26158728]`.
+ If the article is an _arXiv_ preprint, cite like `[@arxiv:1508.06576]`.
+ If the article has none of the above, please file an issue.

You cite multiple items at once like `[@doi:10.15363/thinklab.4 @pmid:26158728
@arxiv:1508.06576]`.

For improved readability, you can (but are not required to) use a tag. For
example, you can add a reference to the tag `Zhou2015_deep_sea` using the
following syntax: `[@tag:Zhou2015_deep_sea]`. If you add references that use
tags, make sure to add those tags and their corresponding citations to
[`references/tags.tsv`](references/tags.tsv).
