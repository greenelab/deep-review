# Building the manuscript

[`build.sh`](build.sh) builds the repository.
`sh build/build.sh` should be executed from the root directory of the repository.
By default, `build.sh` creates HTML and PDF outputs.
However, setting the `BUILD_PDF` environment variable to `false` will suppress PDF output.
For example, run local builds using the command `BUILD_PDF=false sh build/build.sh`.

To build a DOCX file of the manuscript, set the `BUILD_DOCX` environment variable to `true`.
For example, use the command `BUILD_DOCX=true sh build/build.sh`.
To export DOCX for all Travis builds, set a [Travis environment variable](https://docs.travis-ci.com/user/environment-variables/#Defining-Variables-in-Repository-Settings).
Currently, equation numbers via `pandoc-eqnos` are not supported for DOCX output.
There is varying support for embedding images in DOCX output.
Please reference [Pull Request #40](https://github.com/manubot/rootstock/pull/40) for possible solutions and continued discussion.

## Environment

Note: currently, **Windows is not supported**.

Install or update the [conda](https://conda.io) environment specified in [`environment.yml`](environment.yml) by running:

```sh
# If the manubot environment already exists, remove it first
conda env remove --name manubot

# Install the environment
conda env create --file environment.yml
```

Activate with `conda activate manubot` (assumes `conda` version of [at least](https://github.com/conda/conda/blob/9d759d8edeb86569c25f6eb82053f09581013a2a/CHANGELOG.md#440-2017-12-20) 4.4).
The environment should successfully install on both Linux and macOS.
However, it will fail on Windows due to the [`pango`](https://anaconda.org/conda-forge/pango) dependency.
