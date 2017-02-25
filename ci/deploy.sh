set -o errexit

# Configure git
git config --global push.default simple
git config --global user.email "travis@travis-ci.com"
git config --global user.name "Travis CI"
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

# Commit message
message="\
$TRAVIS_COMMIT_MESSAGE

***

The remainder of the commit message has been auto-generated.

TRAVIS_COMMIT=$TRAVIS_COMMIT
TRAVIS_COMMIT_RANGE=$TRAVIS_COMMIT_RANGE

Created by Travis CI build number $TRAVIS_BUILD_NUMBER and job number $TRAVIS_JOB_NUMBER.
https://travis-ci.org/greenelab/deep-review/builds/$TRAVIS_BUILD_ID
https://travis-ci.org/greenelab/deep-review/jobs/$TRAVIS_JOB_ID

Committed on `date --iso-8601=seconds --universal`.
"

# Deploy the reference data to references
ghp-import -p -b references -m $MESSAGE references/generated

# Deploy the output to gh-pages
ghp-import -p -b gh-pages -m $MESSAGE output
