#!/usr/bin/env bash

## install-spellcheck.sh: run during a CI build to install Pandoc spellcheck dependencies.

# Set options for extra caution & debugging
set -o errexit \
    -o pipefail

sudo apt-get update -y
sudo apt-get install -y aspell aspell-en
wget https://raw.githubusercontent.com/pandoc/lua-filters/13c3fa7e97206413609a48a82575cb43137e037f/spellcheck/spellcheck.lua
mv spellcheck.lua build/assets/spellcheck.lua
