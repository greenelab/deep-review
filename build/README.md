# Building the manuscript

[`build.sh`](build.sh) builds the repository.
`bash build/build.sh` should be executed from the root directory of the repository.
By default, `build.sh` creates HTML and PDF outputs.
However, setting the `BUILD_PDF` environment variable to `false` will suppress PDF output.
For example, run local builds using the command `BUILD_PDF=false bash build/build.sh`.

To build a DOCX file of the manuscript, set the `BUILD_DOCX` environment variable to `true`.
For example, use the command `BUILD_DOCX=true bash build/build.sh`.
To export DOCX for all CI builds, set an environment variable (see docs for [GitHub Actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/using-environment-variables) or [Travis CI](https://docs.travis-ci.com/user/environment-variables/#Defining-Variables-in-Repository-Settings)).
Currently, equation numbers via `pandoc-eqnos` are not supported for DOCX output.

Format conversion is done using [Pandoc](https://pandoc.org/MANUAL.html).
`build.sh` calls `pandoc` commands using the options specified in [`pandoc/defaults`](pandoc/defaults).
Each file specifies a set of pandoc `--defaults` options for a given format.
To change the options, either edit the YAML files directly or add additional `--defaults` files.

## Environment

Note: currently, **Windows is not supported**.

Install the [conda](https://conda.io) environment specified in [`environment.yml`](environment.yml) by running the following commands
(from the repository's root directory):

```sh
# Install the environment
conda env create --file build/environment.yml
```

If the `manubot` environment is already installed, but needs to be updated to reflect changes to `environment.yml`, use one of the following options:

```shell
# option 1: update the existing environment.
conda env update --file build/environment.yml

# option 2: remove and reinstall the manubot environment.
# Slower than option 1, but guarantees a fresh environment.
conda env remove --name manubot
conda env create --file build/environment.yml
```

Activate with `conda activate manubot` (assumes `conda` version of [at least](https://github.com/conda/conda/blob/9d759d8edeb86569c25f6eb82053f09581013a2a/CHANGELOG.md#440-2017-12-20) 4.4).
The environment should successfully install on both Linux and macOS.
However, it will fail on Windows due to the [`pango`](https://anaconda.org/conda-forge/pango) dependency.

Because the build process is dependent on having the appropriate version of the `manubot` Python package,
it is necessary to use the version specified in `environment.yml`.
The latest `manubot` release on PyPI may not be compatible with the latest version of this rootstock repository.

## Building PDFs

If Docker is available, `build.sh` uses the [Athena](https://www.athenapdf.com/) [Docker image](https://hub.docker.com/r/arachnysdocker/athenapdf) to build the PDF.
Otherwise, `build.sh` uses [WeasyPrint](https://weasyprint.org/) to build the PDF.
It is common for WeasyPrint to generate many warnings and errors that can be safely ignored.
Examples are shown below:

```text
WARNING: Ignored `pointer-events: none` at 3:16, unknown property.
WARNING: Ignored `font-display:auto` at 1:53114, descriptor not supported.
ERROR: Failed to load font at "https://use.fontawesome.com/releases/v5.7.2/webfonts/fa-brands-400.eot#iefix"
WARNING: Expected a media type, got only/**/screen
```
