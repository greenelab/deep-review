# Exit on errors
set -o errexit

# Add commit hash to the README
envsubst < output/README.md > output/README.md

# Generate OpenTimestamps
python ci/opentimestamps-client/ots stamp \
  output/index.html \
  output/deep-review.pdf \
  output/README.md

# Configure git
git config --global push.default simple
git config --global user.email `git log --max-count=1 --format='%ae'`
git config --global user.name `git log --max-count=1 --format='%an'`
git checkout $TRAVIS_BRANCH
git remote set-url origin git@github.com:greenelab/deep-review.git

# Decrypt and add SSH key
openssl aes-256-cbc \
  -K $encrypted_0dd7e5f24ac8_key \
  -iv $encrypted_0dd7e5f24ac8_iv \
  -in ci/deploy.key.enc \
  -out ci/deploy.key -d
eval `ssh-agent -s`
chmod 600 ci/deploy.key
ssh-add ci/deploy.key

# Fetch and create gh-pages and references branches
# Travis does a shallow and single branch git clone
git remote set-branches --add origin gh-pages references
git fetch origin gh-pages:gh-pages references:references

# Commit message
MESSAGE="\
`git log --max-count=1 --format='%s'`

This build is based on
https://github.com/greenelab/deep-review/commit/$TRAVIS_COMMIT.

This commit was created by the following Travis CI build and job:
https://travis-ci.org/greenelab/deep-review/builds/$TRAVIS_BUILD_ID
https://travis-ci.org/greenelab/deep-review/jobs/$TRAVIS_JOB_ID

[ci skip]

The full commit message that triggered this build is copied below:

$TRAVIS_COMMIT_MESSAGE
"

# Deploy the reference data to references
ghp-import --push --branch=references --message="$MESSAGE" references/generated

# Deploy the output to gh-pages
ghp-import --push --branch=gh-pages --message="$MESSAGE" output
