set -o errexit

# For local convertsion to PDF without any citations use:
# pandoc --verbose --from=markdown --output=review.pdf sections/*.md

jupyter nbconvert --inplace \
  --execute --ExecutePreprocessor.timeout=-1 \
  build/references.ipynb

# pandoc settings
CSL_PATH=https://github.com/citation-style-language/styles/raw/master/plos.csl
BIBLIOGRAPHY_PATH=references/generated/bibliography.json
INPUT_PATH=references/generated/all-sections.md

# Create HTML outpout
# http://pandoc.org/MANUAL.html
pandoc --verbose \
  --from=markdown --to=html \
  --bibliography=$BIBLIOGRAPHY_PATH \
  --csl=$CSL_PATH \
  --output=review.html \
  $INPUT_PATH

# Create PDF outpout
pandoc \
  --from=markdown \
  --to=html5 \
  --bibliography=$BIBLIOGRAPHY_PATH \
  --csl=$CSL_PATH \
  --output=review.pdf \
  $INPUT_PATH
