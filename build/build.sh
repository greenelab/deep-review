set -o errexit

# Generate reference information
echo "Retrieving and processing reference metadata"
(cd build && python references.py)

# pandoc settings
CSL_PATH=https://github.com/citation-style-language/styles/raw/master/dependent/journal-of-the-royal-society-interface.csl
BIBLIOGRAPHY_PATH=references/generated/bibliography.json
INPUT_PATH=references/generated/all-sections.md

# Make output directory
mkdir -p output

# Create HTML outpout
# http://pandoc.org/MANUAL.html
echo "Exporting HTML manuscript"
pandoc --verbose \
  --from=markdown --to=html \
  --bibliography=$BIBLIOGRAPHY_PATH \
  --csl=$CSL_PATH \
  --css=github-pandoc.css \
  --output=output/index.html \
  $INPUT_PATH

# Create PDF outpout
echo "Exporting PDF manuscript"
pandoc \
  --from=markdown \
  --to=html5 \
  --bibliography=$BIBLIOGRAPHY_PATH \
  --csl=$CSL_PATH \
  --output=output/deep-review.pdf \
  $INPUT_PATH
