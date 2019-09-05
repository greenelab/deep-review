#!/usr/bin/env bash

## deploy.sh: run during a Travis CI build to deploy manuscript outputs to the output and gh-pages branches on GitHub.

# Set options for extra caution & debugging
set -o errexit \
    -o nounset \
    -o pipefail

# Add commit hash to the README
OWNER_NAME="$(dirname "$TRAVIS_REPO_SLUG")"
REPO_NAME="$(basename "$TRAVIS_REPO_SLUG")"
export OWNER_NAME REPO_NAME
envsubst < webpage/README.md > webpage/README-complete.md
mv webpage/README-complete.md webpage/README.md

# Configure git
git config --global push.default simple
git config --global user.email "$(git log --max-count=1 --format='%ae')"
git config --global user.name "$(git log --max-count=1 --format='%an')"
git checkout "$TRAVIS_BRANCH"
git remote set-url origin "git@github.com:$TRAVIS_REPO_SLUG.git"

# Decrypt and add SSH key
eval "$(ssh-agent -s)"
(
set +o xtrace  # disable xtrace in subshell for private key operations
if [ -v MANUBOT_SSH_PRIVATE_KEY ]; then
  base64 --decode <<< "$MANUBOT_SSH_PRIVATE_KEY" | ssh-add -
else
echo "DeprecationWarning: Loading deploy.key from an encrypted file.
In the future, using the MANUBOT_SSH_PRIVATE_KEY environment variable may be required."
openssl aes-256-cbc \
  -K $encrypted_9befd6eddffe_key \
  -iv $encrypted_9befd6eddffe_iv \
  -in ci/deploy.key.enc \
  -out ci/deploy.key -d
chmod 600 ci/deploy.key
ssh-add ci/deploy.key
fi
)

# Fetch and create gh-pages and output branches
# Travis does a shallow and single branch git clone
git remote set-branches --add origin gh-pages output
git fetch origin gh-pages:gh-pages output:output

# Configure versioned webpage and timestamp
manubot webpage \
  --timestamp \
  --no-ots-cache \
  --checkout=gh-pages \
  --version="$TRAVIS_COMMIT"

# Commit message
MESSAGE="\
$(git log --max-count=1 --format='%s') [ci skip]

This build is based on
https://github.com/$TRAVIS_REPO_SLUG/commit/$TRAVIS_COMMIT.

This commit was created by the following Travis CI build and job:
$TRAVIS_BUILD_WEB_URL
$TRAVIS_JOB_WEB_URL

The full commit message that triggered this build is copied below:

$TRAVIS_COMMIT_MESSAGE
"

# Deploy the manubot outputs to output
ghp-import \
  --push \
  --branch=output \
  --message="$MESSAGE" \
  output

# Deploy the webpage directory to gh-pages
ghp-import \
  --no-jekyll \
  --follow-links \
  --push \
  --branch=gh-pages \
  --message="$MESSAGE" \
  webpage

# Workaround https://github.com/travis-ci/travis-ci/issues/8082
ssh-agent -k
