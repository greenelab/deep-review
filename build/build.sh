#!/usr/bin/env bash

## build.sh: compile manuscript outputs from content using Manubot and Pandoc

set -o errexit \
    -o nounset \
    -o pipefail

# Set timezone used by Python for setting the manuscript's date
export TZ=Etc/UTC
# Default Python to read/write text files using UTF-8 encoding
export LC_ALL=en_US.UTF-8

# Generate reference information
echo >&2 "Retrieving and processing reference metadata"
manubot process \
  --content-directory=content \
  --output-directory=output \
  --cache-directory=ci/cache \
  --skip-citations \
  --log-level=INFO

# Pandoc's configuration is specified via files of option defaults
# located in the PANDOC_DEFAULTS_DIR directory.
PANDOC_DEFAULTS_DIR="${PANDOC_DEFAULTS_DIR:-build/pandoc-defaults}"

# Make output directory
mkdir -p output

# Create HTML output
# https://pandoc.org/MANUAL.html
echo >&2 "Exporting HTML manuscript"
pandoc --verbose \
  --defaults="$PANDOC_DEFAULTS_DIR/common.yaml" \
  --defaults="$PANDOC_DEFAULTS_DIR/html.yaml"

# Return null if docker command is missing, otherwise return path to docker
DOCKER_EXISTS="$(command -v docker || true)"

# Create PDF output (unless BUILD_PDF environment variable equals "false")
# If Docker is not available, use WeasyPrint to create PDF
if [ "${BUILD_PDF:-}" != "false" ] && [ -z "$DOCKER_EXISTS" ]; then
  echo >&2 "Exporting PDF manuscript using WeasyPrint"
  if [ -L images ]; then rm images; fi  # if images is a symlink, remove it
  ln -s content/images
  pandoc \
    --defaults="$PANDOC_DEFAULTS_DIR/common.yaml" \
    --defaults="$PANDOC_DEFAULTS_DIR/html.yaml" \
    --defaults="$PANDOC_DEFAULTS_DIR/pdf-weasyprint.yaml"
  rm images
fi

# If Docker is available, use athenapdf to create PDF
if [ "${BUILD_PDF:-}" != "false" ] && [ -n "$DOCKER_EXISTS" ]; then
  echo >&2 "Exporting PDF manuscript using Docker + Athena"
  if [ "${CI:-}" = "true" ]; then
    # Incease --delay for CI builds to ensure the webpage fully renders, even when the CI server is under high load.
    # Local builds default to a shorter --delay to minimize runtime, assuming proper rendering is less crucial.
    MANUBOT_ATHENAPDF_DELAY="${MANUBOT_ATHENAPDF_DELAY:-5000}"
    echo >&2 "Continuous integration build detected. Setting athenapdf --delay=$MANUBOT_ATHENAPDF_DELAY"
  fi
  if [ -d output/images ]; then rm -rf output/images; fi  # if images is a directory, remove it
  cp -R -L content/images output/
  docker run \
    --rm \
    --shm-size=1g \
    --volume="$(pwd)/output:/converted/" \
    --security-opt=seccomp:unconfined \
    arachnysdocker/athenapdf:2.16.0 \
    athenapdf \
    --delay=${MANUBOT_ATHENAPDF_DELAY:-1100} \
    --pagesize=A4 \
    manuscript.html manuscript.pdf
  rm -rf output/images
fi

# Create DOCX output (if BUILD_DOCX environment variable equals "true")
if [ "${BUILD_DOCX:-}" = "true" ]; then
  echo >&2 "Exporting Word Docx manuscript"
  pandoc --verbose \
    --defaults="$PANDOC_DEFAULTS_DIR/common.yaml" \
    --defaults="$PANDOC_DEFAULTS_DIR/docx.yaml"
fi

echo >&2 "Build complete"
