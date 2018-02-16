# Exit on errors
set -o errexit

# Add commit hash to the README
export OWNER_NAME=`dirname $TRAVIS_REPO_SLUG`
export REPO_NAME=`basename $TRAVIS_REPO_SLUG`
envsubst < webpage/README.md > webpage/README-complete.md
mv webpage/README-complete.md webpage/README.md

# Configure git
git config --global push.default simple
git config --global user.email `git log --max-count=1 --format='%ae'`
git config --global user.name "`git log --max-count=1 --format='%an'`"
git checkout $TRAVIS_BRANCH
git remote set-url origin git@github.com:$TRAVIS_REPO_SLUG.git

# Decrypt and add SSH key
openssl aes-256-cbc \
  -K $encrypted_f2f00aaf6402_key \
  -iv $encrypted_f2f00aaf6402_iv \
  -in ci/deploy.key.enc \
  -out ci/deploy.key -d
eval `ssh-agent -s`
chmod 600 ci/deploy.key
ssh-add ci/deploy.key

# Fetch and create gh-pages and output branches
# Travis does a shallow and single branch git clone
git remote set-branches --add origin gh-pages output
git fetch origin gh-pages:gh-pages output:output

# Configure versioned webpage
python build/webpage.py \
  --checkout=gh-pages \
  --version=$TRAVIS_COMMIT

# Generate OpenTimestamps
ots stamp \
  webpage/v/$TRAVIS_COMMIT/index.html \
  webpage/v/$TRAVIS_COMMIT/manuscript.pdf

# Commit message
MESSAGE="\
`git log --max-count=1 --format='%s'`

This build is based on
https://github.com/$TRAVIS_REPO_SLUG/commit/$TRAVIS_COMMIT.

This commit was created by the following Travis CI build and job:
https://travis-ci.org/$TRAVIS_REPO_SLUG/builds/$TRAVIS_BUILD_ID
https://travis-ci.org/$TRAVIS_REPO_SLUG/jobs/$TRAVIS_JOB_ID

[ci skip]

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
  --follow-links \
  --push \
  --branch=gh-pages \
  --message="$MESSAGE" \
  webpage

# Workaround https://github.com/travis-ci/travis-ci/issues/8082
ssh-agent -k
