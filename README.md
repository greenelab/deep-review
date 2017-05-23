# Opportunities and obstacles for deep learning in biology and medicine

[![Code Climate](https://codeclimate.com/github/greenelab/deep-review/badges/gpa.svg)](https://codeclimate.com/github/greenelab/deep-review)

We have the opportunity to write a headline review for *Journal of the Royal
Society Interface* on a topic overlapping the computer and life sciences in the
area of systems pharmacology. We are hitting the home stretch towards getting
this paper submitted. Consequently, we have established the following
guidelines:

* April 24: Any empty section, even if in the outline, gets dropped due to lack
  of interest.
* May 1: Any section not merged & ready for revisions gets dropped due to lack
  of completion. Invitations go out to contributing authors to approve the
  manuscript.
* May 1 - 14: Revisions, flow, and clarity.
* Final edits and author approval. Authors must approve by [Noon Eastern
  Time](https://time.is/ET) on May 17 to be included as co-authors. File a pull
  request to add the appropriate line to `author_contact_approval.md`

At this stage it is ideal if **each pull request touches no more than one
subsection** as this minimizes the number of people who will need to sign off on
changes.

The most current version of the `master` branch is built by continuous integration
and [available via gh-pages](https://greenelab.github.io/deep-review/). To see
what's incoming, check the
[open pull requests](https://github.com/greenelab/deep-review/pulls).
If you want to claim a section (time is short - see timeline above!) issue number
[188](https://github.com/greenelab/deep-review/issues/188) is the place to do it.

> A Headline Review is one in a short, targeted series of high-level reviews
within a particular topic of a burgeoning research area. We encourage authors to
write in a style that opens the door to a broad range of readers working at the
physical sciences - life sciences interface. We intend the reviews to address
critical developments in an area of cross-disciplinary research and, when
possible, to place such research in a broader context. This is not a place for
comprehensive literature surveys.
>
> We do encourage you to speculate in an informed way, and to be topical and
provocative about the subject without worrying unduly about space, (the
provisional target length is 8 -12,000 words). Please think of this as an
article which will be a landmark in your area, and will come to be considered as
a classic paper of the literature.

I was recently inspired by [Harold Pimentel's](https://github.com/pimentel)
crowd-sourced [collection of deep learning
papers](https://github.com/pimentel/deep_learning_papers). Instead of having one
individual write this, I thought that this invitation provided a wonderful
opportunity to take advantage of the wisdom of crowds to bring a team together
around this topic.

This repository provides a home for the paper. We'll operate on a pull request
model. Anyone whose contributions meet the ICJME standards of authorship will be
included as an author on the manuscript. I can't guarantee that it will be
accepted, but I look forward to trying this approach out.

## Status Report on 12/21

We are now actively writing the review. Markdown files can be found in the
`sections/` folder. Please claim a section, create a fork, and contribute that
section back via a pull request. To see what a pull request into the paper
entails, check out [PR #147](https://github.com/greenelab/deep-review/pull/147)
from [@evancofer](https://github.com/evancofer).

## Status Report on 10/26

We are now actively outlining the review sections and will begin writing
soon.  The goal is to have a complete draft in about a month.  The action items
from the 8/25 status report below are still applicable.  In addition, you can:

1. Sign up to write in [#116](https://github.com/greenelab/deep-review/issues/116)
   and share which sections you are most interested in.  We are in need of
   experts in biomedical imaging applications in particular.
2. Review the stubs in the `sections` subdirectory and respond to the prompts
   with a pull request.
3. Outline sections that do not have stubs with a pull request and discuss
   them with other co-authors in the pull request comments.

## Status Report on 8/25

Over the first three weeks of this project, we've developed an initial guiding
question; collaboratively read, summarized, and discussed existing literature
through github issues; and we're now refining our guiding question. If you want
to begin to contribute to this review now, there are a few steps that you may
want to take to get up to speed quickly.

1. Read through issue [#2](https://github.com/greenelab/deep-review/issues/2).
   This will give an idea of what our perspective was as we were starting out
   and planning to read papers.
2. Peruse some of the papers that the group has already reviewed, and take a
   look at the review. Fill in gaps that you see in the short summary/discussion
   of the paper.
3. Choose some papers in an area that you care about, review them, and summarize
   them.
4. Dive into [#88](https://github.com/greenelab/deep-review/issues/88) and help
   us to further refine the specific question that we're going to deal with in
   this review.

In about a week, we plan to move into the phase where we start to vigorously
argue about the answer to the question that we coalesce on with
[#88](https://github.com/greenelab/deep-review/issues/88) for each area that the
review will cover.

## Continuous Integration

[![Build Status](https://travis-ci.org/greenelab/deep-review.svg?branch=master)](https://travis-ci.org/greenelab/deep-review)

When you make a pull request, Travis CI will test whether your changes break the build process to generate the formatted manuscript.
The build process aims to detect common errors, such as invalid references.
If your build fails, see the Travis CI logs for the cause of failure and revise your pull request accordingly.

When a pull request is merged, Travis CI performs the build and writes the results to the [`gh-pages`](https://github.com/greenelab/deep-review/tree/gh-pages) and [`references`](https://github.com/greenelab/deep-review/tree/references) branches.
The `gh-pages` branch hosts the following URLs:

+ **HTML manuscript** at https://greenelab.github.io/deep-review/<br>
  short URL: https://git.io/vytJN
+ **PDF manuscript** at https://greenelab.github.io/deep-review/deep-review.pdf<br>
  short URL: https://git.io/vytJ5

For continuous integration configuration details, see [`.travis.yml`](.travis.yml).

## License

[![License: CC BY 4.0](https://img.shields.io/badge/License%20All-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/)
[![License: CC0 1.0](https://img.shields.io/badge/License%20Parts-CC0%201.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

This entirety of this repository is licensed under a CC BY 4.0 License ([`LICENSE.md`](LICENSE.md)), which allows reuse with attribution.
Please attribute by linking to https://github.com/greenelab/deep-review.

Since CC BY is not ideal for code and data, certain repository components are also released under the CC0 1.0 public domain dedication ([`LICENSE-CC0.md`](LICENSE-CC0.md)).
All files matched by the following blog patterns are dual licensed under CC BY 4.0 and CC0 1.0:

+ `*.sh`
+ `*.py`
+ `*.yml`
+ `*.json`
+ `*.bib`
+ `*.tsv`
+ `.gitignore`

All other files are only available under CC BY 4.0, including:

+ `*.md`
+ `*.html`
+ `*.pdf`

Please open [an issue](https://github.com/greenelab/deep-review/issues) for any question related to licensing.
