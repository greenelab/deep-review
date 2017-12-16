# Building the manuscript

[`build.sh`](build.sh) builds the repository.
`sh build.sh` should be executed from the root directory of the repository.

To build a DOCX file of the manuscript, set the `BUILD_DOCX` environment variable to `true`.
For example, use the command `BUILD_DOCX=true sh build/build.sh`.
Set a [Travis environment variable](https://docs.travis-ci.com/user/environment-variables/#Defining-Variables-in-Repository-Settings) to export DOCX for all Travis builds.
Currently, equation numbers via `pandoc-eqnos` are not supported for DOCX output.
There is varying support for embedding images in DOCX output.
Please reference [Pull Request #40](https://github.com/greenelab/manubot-rootstock/pull/40) for possible solutions and continued discussion.

## Environment

Install the [conda](https://conda.io) environment specified in [`environment.yml`](environment.yml) by running:

```sh
conda env create --file environment.yml
```

Activate with `source activate manubot`.
Currently, the environment requires Linux.
