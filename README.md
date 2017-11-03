# Opportunities and obstacles for deep learning in biology and medicine

[![HTML Manuscript](https://img.shields.io/badge/manuscript-HTML-blue.svg)](https://greenelab.github.io/deep-review/)
[![PDF Manuscript](https://img.shields.io/badge/manuscript-PDF-blue.svg)](https://greenelab.github.io/deep-review/manuscript.pdf)
[![Build Status](https://travis-ci.org/greenelab/deep-review.svg?branch=master)](https://travis-ci.org/greenelab/deep-review)
[![Code Climate](https://codeclimate.com/github/greenelab/deep-review/badges/gpa.svg)](https://codeclimate.com/github/greenelab/deep-review)

## Manuscript description

To see what's incoming, check the [open pull requests](https://github.com/greenelab/deep-review/pulls).

#### Current Status - Submitted

We have submitted the manuscript to the journal. A preprint is available at
[bioRxiv](https://doi.org/10.1101/142760). We are still accepting contributions
to improve this work. Feel free to create an issue, contribute some text via a
pull request, and pitch in. Authorship criteria remain the same.

#### More about the manuscript.

We have the opportunity to write a headline review for *Journal of the Royal
Society Interface* on a topic overlapping the computer and life sciences in the
area of systems pharmacology.

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

#### Status Report on 12/21

We are now actively writing the review. Markdown files can be found in the
`sections/` folder. Please claim a section, create a fork, and contribute that
section back via a pull request. To see what a pull request into the paper
entails, check out [PR #147](https://github.com/greenelab/deep-review/pull/147)
from [@evancofer](https://github.com/evancofer).

#### Status Report on 10/26

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

#### Status Report on 8/25

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

## Manubot

<!-- usage note: do not edit this section -->

Manubot is a system for writing scholarly manuscripts via GitHub.
Manubot automates citations and references, versions manuscripts using git, and enables collaborative writing via GitHub.
The [Manubot Rootstock repository](https://git.io/vQSvo) is a general purpose template for creating new Manubot instances, as detailed in [`SETUP.md`](SETUP.md).
See [`USAGE.md`](USAGE.md) for documentation how to write a manuscript.

### Repository directories & files

The directories are as follows:

+ [`content`](content) contains the manuscript source, which includes markdown files as well as inputs for citations and references.
  See [`USAGE.md`](USAGE.md) for more information.
+ [`output`](output) contains the outputs (generated files) from the manubot including the resulting manuscripts.
  You should not edit these files manually, because they will get overwritten.
+ [`webpage`](webpage) is a directory meant to be rendered as a static webpage for viewing the HTML manuscript.
+ [`build`](build) contains commands and tools for building the manuscript.
+ [`ci`](ci) contains files necessary for deployment via continuous integration.
  For the CI configuration, see [`.travis.yml`](.travis.yml).

### Local execution

To run the Manubot locally, install the [conda](https://conda.io) environment as described in [`build`](build).
Then, you can build the manuscript on POSIX systems by running the following commands.

```sh
# Activate the manubot conda environment
source activate manubot

# Build the manuscript
sh build/build.sh

# Or monitor the content directory, and automatically rebuild the manuscript
# when a change is detected.
sh build/autobuild.sh

# View the manuscript locally at http://localhost:8000/
cd webpage
python -m http.server
```

### Continuous Integration

[![Build Status](https://travis-ci.org/greenelab/deep-review.svg?branch=master)](https://travis-ci.org/greenelab/deep-review)

Whenever a pull request is opened, Travis CI will test whether the changes break the build process to generate a formatted manuscript.
The build process aims to detect common errors, such as invalid citations.
If your pull request build fails, see the Travis CI logs for the cause of failure and revise your pull request accordingly.

When a commit to the `master` branch occurs (for example, when a pull request is merged), Travis CI builds the manuscript and writes the results to the [`gh-pages`](https://github.com/greenelab/deep-review/tree/gh-pages) and [`output`](https://github.com/greenelab/deep-review/tree/output) branches.
The `gh-pages` branch uses [GitHub Pages](https://pages.github.com/) to host the following URLs:

+ **HTML manuscript** at https://greenelab.github.io/deep-review/
+ **PDF manuscript** at https://greenelab.github.io/deep-review/manuscript.pdf

For continuous integration configuration details, see [`.travis.yml`](.travis.yml).

## License

[![License: CC BY 4.0](https://img.shields.io/badge/License%20All-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/)
[![License: CC0 1.0](https://img.shields.io/badge/License%20Parts-CC0%201.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

Except when noted otherwise, the entirety of this repository is licensed under a CC BY 4.0 License ([`LICENSE.md`](LICENSE.md)), which allows reuse with attribution.
Please attribute by linking to https://github.com/greenelab/deep-review.

Since CC BY is not ideal for code and data, certain repository components are also released under the CC0 1.0 public domain dedication ([`LICENSE-CC0.md`](LICENSE-CC0.md)).
All files matched by the following glob patterns are dual licensed under CC BY 4.0 and CC0 1.0:

+ `*.sh`
+ `*.py`
+ `*.yml` / `*.yaml`
+ `*.json`
+ `*.bib`
+ `*.tsv`
+ `.gitignore`

All other files are only available under CC BY 4.0, including:

+ `*.md`
+ `*.html`
+ `*.pdf`
+ `*.docx`

Except for the following files with different licenses:

+ `build/assets/anchors.js` which is [released](https://www.bryanbraun.com/anchorjs/) under an [MIT License](https://opensource.org/licenses/MIT)

Please open [an issue](https://github.com/greenelab/deep-review/issues) for any question related to licensing.
