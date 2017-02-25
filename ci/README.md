# Continuous integration / analysis directory

[![Build Status](https://travis-ci.org/greenelab/deep-review.svg?branch=master)](https://travis-ci.org/greenelab/deep-review)

This repository uses [continuous analysis](https://doi.org/10.1101/056473 "Reproducible Computational Workflows with Continuous Analysis") to create the manuscript and commit it back to GitHub.

## Generating the GitHub deploy key

To generate and configure the GitHub SSH deploy key, run the following commands from this directory.

```sh
# Generate a new SSH key
ssh-keygen -t rsa -b 4096 -C "travis@travis-ci.com" -f deploy.sh
# Add deploy.key.pub to GitHub under the repository's settings
# see https://developer.github.com/guides/managing-deploy-keys/#deploy-keys

# Encrypt and upload key to Travis CI.
# See https://docs.travis-ci.com/user/encrypting-files/
travis encrypt-file deploy.key
# Modify the returned command to decrypt the key in ci/deploy.sh
```
