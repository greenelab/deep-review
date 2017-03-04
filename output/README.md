# Output directory containing the formatted manuscript

The [`gh-pages`](https://github.com/greenelab/deep-review/tree/gh-pages) branch hosts the contents of this directory at https://greenelab.github.io/deep-review/.

## Files

This directory contains the following files, which are mostly ignored on the `master` branch:

+ [`index.html`](index.html) is an HTML manuscript.
+ [`github-pandoc.css`](github-pandoc.css) sets the display style for `index.html`.
+ [`deep-review.pdf`](deep-review.pdf) is a PDF manuscript.
+ `*.ots` files are OpenTimestamps which can be used to verify manuscript existence at or before a given time.
  [OpenTimestamps](opentimestamps.org) uses the Bitcoin blockchain to attest to file hash existence.

## Source

The manuscripts in this directory were built from
[`$TRAVIS_COMMIT`](https://github.com/greenelab/deep-review/commit/$TRAVIS_COMMIT).
