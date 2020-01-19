#!/usr/bin/env bash

## deploy.sh: run during a Travis CI build to deploy manuscript outputs to the output and gh-pages branches on GitHub.

# Set options for extra caution & debugging
set -o errexit \
    -o nounset \
    -o pipefail

# set environment variables for either Travis or GitHub Actions
REPO_SLUG=${TRAVIS_REPO_SLUG:-$GITHUB_REPOSITORY}
COMMIT=${TRAVIS_COMMIT:-$GITHUB_SHA}
BUILD_WEB_URL=${TRAVIS_BUILD_WEB_URL:-$BUILD_WEB_URL}
JOB_WEB_URL=${TRAVIS_JOB_WEB_URL:-"https://github.com/$GITHUB_REPOSITORY/runs/$GITHUB_ACTION"}
BRANCH=${TRAVIS_BRANCH:-master}

# Add commit hash to the README
OWNER_NAME="$(dirname "$REPO_SLUG")"
REPO_NAME="$(basename "$REPO_SLUG")"
export OWNER_NAME REPO_NAME
envsubst < webpage/README.md > webpage/README-complete.md
mv webpage/README-complete.md webpage/README.md

# Configure git
git config --global push.default simple
git config --global user.email "$(git log --max-count=1 --format='%ae')"
git config --global user.name "$(git log --max-count=1 --format='%an')"
git checkout "$BRANCH"
git remote set-url origin "git@github.com:$REPO_SLUG.git"

# Decrypt and add SSH key
eval "$(ssh-agent -s)"
(
set +o xtrace  # disable xtrace in subshell for private key operations
if [ -v MANUBOT_SSH_PRIVATE_KEY ]; then
  base64 --decode <<< "$MANUBOT_SSH_PRIVATE_KEY" | ssh-add -
else
echo >&2 "DeprecationWarning: Loading deploy.key from an encrypted file.
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
  --version="$COMMIT"

# Commit message
MESSAGE="\
$(git log --max-count=1 --format='%s')
[ci skip]

This build is based on
https://github.com/$REPO_SLUG/commit/$COMMIT.

This commit was created by the following CI build and job:
$BUILD_WEB_URL
$JOB_WEB_URL
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
