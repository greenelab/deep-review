set -o errexit

# Set timezone used by Python for setting the manuscript's date
export TZ=Etc/UTC
# Default Python to read/write text files using UTF-8 encoding
export LC_ALL=en_US.UTF-8

# Generate reference information
echo "Retrieving and processing reference metadata"
manubot \
  --content-directory=content \
  --output-directory=output \
  --cache-directory=ci/cache \
  --log-level=INFO

# pandoc settings
CSL_PATH=build/assets/style.csl
DOCX_PATH=build/assets/pandoc-reference.docx
BIBLIOGRAPHY_PATH=output/references.json
INPUT_PATH=output/manuscript.md

# Make output directory
mkdir -p output

# Create HTML output
# http://pandoc.org/MANUAL.html
echo "Exporting HTML manuscript"
pandoc --verbose \
  --from=markdown \
  --to=html5 \
  --filter=pandoc-fignos \
  --filter=pandoc-eqnos \
  --filter=pandoc-tablenos \
  --bibliography=$BIBLIOGRAPHY_PATH \
  --csl=$CSL_PATH \
  --metadata link-citations=true \
  --mathjax \
  --css=github-pandoc.css \
  --include-in-header=build/assets/analytics.html \
  --include-after-body=build/assets/anchors.html \
  --include-after-body=build/assets/hypothesis.html \
  --output=output/manuscript.html \
  $INPUT_PATH

# Create PDF output
echo "Exporting PDF manuscript"
ln -s content/images images
pandoc \
  --from=markdown \
  --to=html5 \
  --pdf-engine=weasyprint \
  --pdf-engine-opt=--presentational-hints \
  --filter=pandoc-fignos \
  --filter=pandoc-eqnos \
  --filter=pandoc-tablenos \
  --bibliography=$BIBLIOGRAPHY_PATH \
  --csl=$CSL_PATH \
  --metadata link-citations=true \
  --webtex=https://latex.codecogs.com/svg.latex? \
  --css=webpage/github-pandoc.css \
  --output=output/manuscript.pdf \
  $INPUT_PATH
rm -r images

# Create DOCX output when user specifies to do so
if [ "$BUILD_DOCX" = "true" ];
then
    echo "Exporting Word Docx manuscript"
    pandoc --verbose \
    --from=markdown \
    --to=docx \
    --filter=pandoc-fignos \
    --filter=pandoc-eqnos \
    --filter=pandoc-tablenos \
    --bibliography=$BIBLIOGRAPHY_PATH \
    --csl=$CSL_PATH \
    --metadata link-citations=true \
    --reference-doc=$DOCX_PATH \
    --resource-path=.:content \
    --output=output/manuscript.docx \
    $INPUT_PATH
fi

echo "Build complete"
