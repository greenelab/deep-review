# The Deep Review

[![HTML Manuscript](https://img.shields.io/badge/manuscript-HTML-blue.svg)](https://greenelab.github.io/deep-review/)
[![PDF Manuscript](https://img.shields.io/badge/manuscript-PDF-blue.svg)](https://greenelab.github.io/deep-review/manuscript.pdf)
[![GitHub Actions Status](https://github.com/greenelab/deep-review/workflows/Manubot/badge.svg)](https://github.com/greenelab/deep-review/actions)
[![Code Climate](https://codeclimate.com/github/greenelab/deep-review/badges/gpa.svg)](https://codeclimate.com/github/greenelab/deep-review)

## Manuscript description

This repository is home to the **Deep Review**, a review article on deep learning in precision medicine.
The Deep Review is collaboratively written on GitHub using a tool called Manubot (see [below](#manubot)).
The project operates on an open contribution model, welcoming contributions from anyone (see [`CONTRIBUTING.md`](CONTRIBUTING.md) or an [existing example](https://github.com/greenelab/deep-review/pull/147 "Pull request 147: Hardware Limitations and Scaling") for more info).
To see what's incoming, check the open [pull requests](https://github.com/greenelab/deep-review/pulls).
For project discussion and planning see the [Issues](https://github.com/greenelab/deep-review/issues).

The original version of the Deep Review was published in 2018 and should be cited as:
> Ching T, Himmelstein DS, Beaulieu-Jones BK, Kalinin AA, Do BT, Way GP, Ferrero E, Agapow P-M, Zietz M, Hoffman MM, Xie W, Rosen GL, Lengerich BJ, Israeli J, Lanchantin J, Woloszynek S, Carpenter AE, Shrikumar A, Xu J, Cofer EM, Lavender CA, Turaga SC, Alexandari AM, Lu Z, Harris DJ, DeCaprio D, Qi Y, Kundaje A, Peng Y, Wiley LK, Segler MHS, Boca SM, Swamidass SJ, Huang A, Gitter A, and Greene CS. 2018. Opportunities and obstacles for deep learning in biology and medicine. _Journal of The Royal Society Interface_ 15(141):20170387. [doi:10.1098/rsif.2017.0387](https://doi.org/10.1098/rsif.2017.0387)


### Current stage: planning Deep Review version 2.0

As of writing, we are aiming to publish an update of the deep review.
We will continue to make project preprints available on bioRxiv or another preprint service and aim to continue publishing the finished reviews in a peer-reviewed venue as well.
Like the initial release, we are planning for an open and collaborative effort.
New contributors are welcome and will be listed as version 2.0 authors.
Please see [issue #810](https://github.com/greenelab/deep-review/issues/810) to contribute to the discussion of future plans, and help decide how to best continue this project.

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

The [initial manuscript](https://doi.org/10.1098/rsif.2017.0387) was a headline review for [_Journal of the Royal Society Interface_](http://rsif.royalsocietypublishing.org/) on a topic overlapping the computer and life sciences in the area of systems pharmacology.
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

On August 5, Deep Review was announced with a [tweet](https://twitter.com/GreeneScientist/status/761606546774163456).

## Manubot

<!-- usage note: do not edit this section -->

Manubot is a system for writing scholarly manuscripts via GitHub.
Manubot automates citations and references, versions manuscripts using git, and enables collaborative writing via GitHub.
An [overview manuscript](https://greenelab.github.io/meta-review/ "Open collaborative writing with Manubot") presents the benefits of collaborative writing with Manubot and its unique features.
The [rootstock repository](https://git.io/fhQH1) is a general purpose template for creating new Manubot instances.
See [`USAGE.md`](USAGE.md) for documentation how to write a manuscript.

Please open [an issue](https://git.io/fhQHM) for questions related to Manubot usage, bug reports, or general inquiries.

### Repository directories & files

The directories are as follows:

+ [`content`](content) contains the manuscript source, which includes markdown files as well as inputs for citations and references.
  See [`USAGE.md`](USAGE.md) for more information.
+ [`output`](output) contains the outputs (generated files) from Manubot including the resulting manuscripts.
  You should not edit these files manually, because they will get overwritten.
+ [`webpage`](webpage) is a directory meant to be rendered as a static webpage for viewing the HTML manuscript.
+ [`build`](build) contains commands and tools for building the manuscript.
+ [`ci`](ci) contains files necessary for deployment via continuous integration.

### Local execution

The easiest way to run Manubot is to use [continuous integration](#continuous-integration) to rebuild the manuscript when the content changes.
If you want to build a Manubot manuscript locally, install the [conda](https://conda.io) environment as described in [`build`](build).
Then, you can build the manuscript on POSIX systems by running the following commands from this root directory.

```sh
# Activate the manubot conda environment (assumes conda version >= 4.4)
conda activate manubot

# Build the manuscript, saving outputs to the output directory
bash build/build.sh

# At this point, the HTML & PDF outputs will have been created. The remaining
# commands are for serving the webpage to view the HTML manuscript locally.
# This is required to view local images in the HTML output.

# Configure the webpage directory
manubot webpage

# You can now open the manuscript webpage/index.html in a web browser.
# Alternatively, open a local webserver at http://localhost:8000/ with the
# following commands.
cd webpage
python -m http.server
```

Sometimes it's helpful to monitor the content directory and automatically rebuild the manuscript when a change is detected.
The following command, while running, will trigger both the `build.sh` script and `manubot webpage` command upon content changes:

```sh
bash build/autobuild.sh
```

### Continuous Integration

Whenever a pull request is opened, CI (continuous integration) will test whether the changes break the build process to generate a formatted manuscript.
The build process aims to detect common errors, such as invalid citations.
If your pull request build fails, see the CI logs for the cause of failure and revise your pull request accordingly.

When a commit to the `master` branch occurs (for example, when a pull request is merged), CI builds the manuscript and writes the results to the [`gh-pages`](https://github.com/greenelab/deep-review/tree/gh-pages) and [`output`](https://github.com/greenelab/deep-review/tree/output) branches.
The `gh-pages` branch uses [GitHub Pages](https://pages.github.com/) to host the following URLs:

+ **HTML manuscript** at https://greenelab.github.io/deep-review/
+ **PDF manuscript** at https://greenelab.github.io/deep-review/manuscript.pdf

For continuous integration configuration details, see [`.github/workflows/manubot.yaml`](.github/workflows/manubot.yaml) if using GitHub Actions or [`.travis.yml`](.travis.yml) if using Travis CI.

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

Please open [an issue](https://github.com/greenelab/deep-review/issues) for any question related to licensing.
