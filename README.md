# The Deep Review

[![HTML Manuscript](https://img.shields.io/badge/manuscript-HTML-blue.svg)](https://greenelab.github.io/deep-review/)
[![PDF Manuscript](https://img.shields.io/badge/manuscript-PDF-blue.svg)](https://greenelab.github.io/deep-review/manuscript.pdf)
[![Build Status](https://travis-ci.org/greenelab/deep-review.svg?branch=master)](https://travis-ci.org/greenelab/deep-review)
[![Code Climate](https://codeclimate.com/github/greenelab/deep-review/badges/gpa.svg)](https://codeclimate.com/github/greenelab/deep-review)

## Manuscript description

This repository is home to **The Deep Review**, a collaboratively written review article on deep learning in precision medicine.
The preprint for this study, titled **Opportunities and obstacles for deep learning in biology and medicine**, is [available on _bioRxiv_](https://doi.org/10.1101/142760).
The Deep Review is collaboratively written on GitHub using a tool called Manubot (see [below](#manubot)).
The project operates on an open contribution model, welcoming contributions from anyone (see [`CONTRIBUTING.md`](CONTRIBUTING.md) or an [existing example](https://github.com/greenelab/deep-review/pull/147 "Pull request 147: Hardware Limitations and Scaling") for more info).
To see what's incoming, check the open [pull requests](https://github.com/greenelab/deep-review/pulls).
For project discussion and planning see the [Issues](https://github.com/greenelab/deep-review/issues).

### Current stage: resubmitted to _JRSI_ and _bioRxiv_

We [completed](https://github.com/greenelab/deep-review/releases/tag/v0.10) manuscript revisions in [response](content/response-to-reviewers.md) to two external peer reviews.
Please see [issue #810](https://github.com/greenelab/deep-review/issues/810) for a discussion about future plans and whether we will continue to accept new pull requests.

**Manubot updates:**
We recently [updated](https://github.com/greenelab/deep-review/pull/681) this repository to use the latest Manubot version.
Citations must now be semicolon separated like `[@doi:10.1002/minf.201501008; @doi:10.1002/jcc.24764]` and citation tags are required when the identifier contains [forbidden characters](USAGE.md#citation-tags).
Previously, multiple citations were just separated by whitespace.
In addition, we're switching from wrapping text at a character cutoff to "one sentence per line" as described in [`USAGE.md`](USAGE.md).
Please make sure you base your pull requests off of the latest version of the `greenelab:master` branch.
Keep your fork synced by [setting](https://help.github.com/articles/configuring-a-remote-for-a-fork/) its `upstream` remote to `greenelab` and running:

```sh
# If your branch only has commits from greenelab:master but is outdated
git pull --ff-only upstream master

# If your branch is outdated and has diverged from greenelab:master
git pull --rebase upstream master
```

### Headline review format

The manuscript is intended to be a headline review for [_Journal of the Royal Society Interface_](http://rsif.royalsocietypublishing.org/) on a topic overlapping the computer and life sciences in the area of systems pharmacology.
The headline review solicitation states:

> A Headline Review is one in a short, targeted series of high-level reviews within a particular topic of a burgeoning research area.
We encourage authors to write in a style that opens the door to a broad range of readers working at the
physical sciences - life sciences interface.
We intend the reviews to address critical developments in an area of cross-disciplinary research and, when possible, to place such research in a broader context.
This is not a place for comprehensive literature surveys.
>
> We do encourage you to speculate in an informed way, and to be topical and provocative about the subject without worrying unduly about space, (the provisional target length is 8-12,000 words).
Please think of this as an article which will be a landmark in your area, and will come to be considered as a classic paper of the literature.

### Inspiration

On August 2, 2016, project maintainer [Casey Greene](https://github.com/cgreene) introduced the project and its motivations:

> I was recently inspired by [Harold Pimentel's](https://github.com/pimentel) crowd-sourced [collection of deep learning papers](https://github.com/pimentel/deep_learning_papers).
Instead of having one individual write this, I thought that this invitation provided a wonderful opportunity to take advantage of the wisdom of crowds to bring a team together around this topic.
>
> This repository provides a home for the paper.
We'll operate on a pull request model.
Anyone whose contributions meet the ICJME standards of authorship will be included as an author on the manuscript.
I can't guarantee that it will be accepted, but I look forward to trying this approach out.

## Manubot

<!-- usage note: do not edit this section -->

Manubot is a system for writing scholarly manuscripts via GitHub.
Manubot automates citations and references, versions manuscripts using git, and enables collaborative writing via GitHub.
The [Manubot Rootstock repository](https://git.io/vQSvo) is a general purpose template for creating new Manubot instances.
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
# Activate the manubot conda environment (assumes conda version >= 4.4)
conda activate manubot

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
