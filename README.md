# Continuous manuscripts written collaboratively on GitHub

[Manubot Rootstock](https://git.io/vQSvo) provides a system for collaboratively writing scholarly manuscripts via GitHub.
This project aims to automate publishing.
For example, citation and referencing are largely automated.
This project originated with the [Deep Review](https://github.com/greenelab/deep-review), but was moved here in hopes of making a general purpose template for the system.

A rootstock (or rhizome) is "a plant onto which another variety is grafted".
This repository plays the role of a botanical trunk.
Fork it and a manuscript will grow.

The most current version of the `master` branch is built by continuous integration and [available via gh-pages](https://greenelab.github.io/manubot-rootstock/).
To see what's incoming, check the [open pull requests](https://github.com/greenelab/manubot-rootstock/pulls).

Instructions for using Manubot Rootstock for your own manuscript are still evolving.
The recommended approach is to clone this repository, as detailed [here](https://github.com/greenelab/manubot-rootstock/issues/6#issuecomment-314541837).

## Repository directories & files

See [`USAGE.md`](USAGE.md) for documentation on how to create or contribute to a manuscript.

The directories are as follows:

+ [`content`](content) contains the manuscript source, which includes markdown files as well as inputs for citations and references.
+ [`output`](output) contains the outputs (generated files) from the manubot including the resulting manuscripts.
  You should not edit these files manually, because they will get overwritten.
+ [`webpage`](webpage) is a directory meant to be rendered as a static webpage for viewing the HTML manuscript.
+ [`build`](build) contains commands and tools for building the manuscript.
+ [`ci`](ci) contains files necessary for deployment via continuous integration.
  For the CI configuration, see [`.travis.yml`](.travis.yml).

## Local execution

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

## Continuous Integration

[![Build Status](https://travis-ci.org/greenelab/manubot-rootstock.svg?branch=master)](https://travis-ci.org/greenelab/manubot-rootstock)

When you make a pull request, Travis CI will test whether your changes break the build process to generate the formatted manuscript.
The build process aims to detect common errors, such as invalid references.
If your build fails, see the Travis CI logs for the cause of failure and revise your pull request accordingly.

When a pull request is merged, Travis CI performs the build and writes the results to the [`gh-pages`](https://github.com/greenelab/manubot-rootstock/tree/gh-pages) and [`output`](https://github.com/greenelab/manubot-rootstock/tree/output) branches.
The `gh-pages` branch hosts the following URLs:

+ **HTML manuscript** at https://greenelab.github.io/manubot-rootstock/
+ **PDF manuscript** at https://greenelab.github.io/manubot-rootstock/manuscript.pdf

For continuous integration configuration details, see [`.travis.yml`](.travis.yml).

## License

[![License: CC BY 4.0](https://img.shields.io/badge/License%20All-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/)
[![License: CC0 1.0](https://img.shields.io/badge/License%20Parts-CC0%201.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

This entirety of this repository is licensed under a CC BY 4.0 License ([`LICENSE.md`](LICENSE.md)), which allows reuse with attribution.
Please attribute by linking to https://github.com/greenelab/manubot-rootstock.

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

Please open [an issue](https://github.com/greenelab/manubot-rootstock/issues) for any question related to licensing.
