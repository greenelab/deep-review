# Continuous integration / analysis directory

[![Build Status](https://travis-ci.org/greenelab/manubot-rootstock.svg?branch=master)](https://travis-ci.org/greenelab/manubot-rootstock)

This repository uses [continuous analysis](https://doi.org/10.1101/056473 "Reproducible Computational Workflows with Continuous Analysis") to create the manuscript and commit it back to GitHub.
[`deploy.sh`](deploy.sh) runs on successful `master` branch builds that are not pull requests.
The contents of `/output` are committed to the `gh-pages` branch.
The contents of `/references/generated` are committed to the `references` branch.

## Generating the GitHub deploy key

To generate and configure the GitHub SSH deploy key, run the following commands from this directory.

```sh
# Generate a new SSH key
ssh-keygen \
  -t rsa \
  -b 4096 \
  -C "travis@travis-ci.com" \
  -N "" \
  -f deploy.key
# Add deploy.key.pub to GitHub under the repository's settings
# see https://developer.github.com/guides/managing-deploy-keys/#deploy-keys

# Encrypt and upload key to Travis CI.
# See https://docs.travis-ci.com/user/encrypting-files/
travis encrypt-file deploy.key
# Modify the returned command to decrypt the key in ci/deploy.sh
```
