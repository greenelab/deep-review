set -o errexit

# Default Python to read/write text files using UTF-8 encoding
export LC_ALL=en_US.UTF-8

# Generate reference information
echo "Retrieving and processing reference metadata"
(cd build && python references.py)

# pandoc settings
CSL_PATH=references/style.csl
BIBLIOGRAPHY_PATH=references/generated/bibliography.json
INPUT_PATH=references/generated/all-sections.md
LINK_COLOR='blue'

# Make output directory
mkdir -p output

# Create HTML output
# http://pandoc.org/MANUAL.html
echo "Exporting HTML manuscript"
pandoc --verbose \
  --from=markdown \
  --to=html \
  --filter pandoc-fignos \
  --filter pandoc-eqnos \
  --filter pandoc-tablenos \
  --bibliography=$BIBLIOGRAPHY_PATH \
  --csl=$CSL_PATH \
  --metadata link-citations=true \
  --css=github-pandoc.css \
  --include-in-header=build/assets/analytics.js \
  --include-after-body=build/assets/anchors.js \
  --output=output/index.html \
  $INPUT_PATH

# Create PDF output
echo "Exporting PDF manuscript"
pandoc \
  --from=markdown \
  --to=html5 \
  --filter pandoc-fignos \
  --filter pandoc-eqnos \
  --filter pandoc-tablenos \
  --bibliography=$BIBLIOGRAPHY_PATH \
  --csl=$CSL_PATH \
  --metadata link-citations=true \
  --output=output/manuscript.pdf \
  $INPUT_PATH

