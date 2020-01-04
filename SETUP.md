# Cloning the manubot/rootstock repository to create a new manuscript

The process to create a new Manubot manuscript is a bit challenging, because it requires a few steps that are difficult to automate.
However, you will only have to perform these steps once for each manuscript.
These steps should be performed in a command-line shell (terminal), starting in the directory where you want the manuscript folder be created.
Setup is supported on Linux, macOS, and Windows.
Windows setup requires [Git Bash](https://gitforwindows.org/) or [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/faq).

## Configuration

First, you must configure two environment variables (`OWNER` and `REPO`).
These variables specify the GitHub repository for the manuscript (i.e. `https://github.com/OWNER/REPO`).
Make sure that the case of `OWNER` matches how your username is displayed on GitHub.
In general, assume that all commands in this setup are case-sensitive.
**Edit the following commands with your manuscript's information:**

```sh
# GitHub username (change from manubot)
OWNER=manubot
# Repository name (change from rootstock)
REPO=rootstock
```

## Create repository

**Execute the remaining commands verbatim.**
They do not need to be edited (if the setup works as intended).

Next you must clone `manubot/rootstock` and configure its branches and remotes:

```sh
# Clone manubot/rootstock
git clone https://github.com/manubot/rootstock.git $REPO
cd $REPO

# Configure remotes and branches
git remote add rootstock https://github.com/manubot/rootstock.git
git checkout --orphan gh-pages
git rm -r --force .
git commit --allow-empty \
  --message "Initialize empty branch" \
  --message "[ci skip]"
git checkout -b output
git checkout master

# Option A: Set origin URL using its web address
git remote set-url origin https://github.com/$OWNER/$REPO.git
# Option B: If GitHub SSH key access is enabled for OWNER, run the following command instead
git remote set-url origin git@github.com:$OWNER/$REPO.git
```

Next, you must manually create an empty GitHub repository at <https://github.com/new>.
Make sure to use the same "Owner" and "Repository name" specified above.
Do not initialize the repository, other than optionally adding a Description.
Next, push your cloned manuscript:

```sh
git push --set-upstream origin master
git push --set-upstream origin gh-pages
git push --set-upstream origin output
```

## Continuous integration

Now you must manually enable Travis CI for the new repository at <https://travis-ci.com>.
Click the `+` sign to "Add New Repository".
If you don't see your repository listed, push the "Sync account" button.
Finally, flick the repository's switch to enable CI.

### Deploy key

Generate a deploy key so Travis CI can write to the repository.

```sh
# IMPORTANT: change working directory to ci
cd ci

# Generate deploy.key.pub (public) and deploy.key (private)
ssh-keygen \
  -t rsa -b 4096 -N "" \
  -C "deploy@travis-ci.com" \
  -f deploy.key

# Encode deploy.key to remove newlines, writing encoded text to deploy.key.txt.
# This is required for entry into the Travis settings.
openssl base64 -A -in deploy.key > deploy.key.txt
```

#### Add the public key to GitHub

```sh
# Print the URL for adding the public key to GitHub
echo "https://github.com/$OWNER/$REPO/settings/keys/new"

# Print the public key for copy-pasting to GitHub
cat deploy.key.pub
```

Go to the GitHub settings URL echoed above in a browser, and click "Add deploy key".
For "Title", add a description like "Manubot Travis Deploy Key".
Copy-paste the contents of the `deploy.key.pub` text file (printed above by `cat`) into the "Key" text box.
Check the "Allow write access" box below.
Finally, click "Add key".

#### Add the private key to Travis CI

```sh
# Print the URL for adding the private key to Travis CI
echo "https://travis-ci.com/$OWNER/$REPO/settings"

# Print the encoded private key for copy-pasting to Travis CI
cat deploy.key.txt && echo
```

Next, go to the Travis CI repository settings page (URL echoed above).
Add a new record in the "Environment Variables" section.
For "NAME", enter `MANUBOT_SSH_PRIVATE_KEY`.
Next, copy-paste the content of `deploy.key.txt` into "VALUE"
(printed above by `cat`, including any trailing `=` characters if present).
Make sure "Display value in build logs" remains toggled off (the default).

While in the Travis CI settings, activate the [limit concurrent jobs](https://blog.travis-ci.com/2014-07-18-per-repository-concurrency-setting/) toggle and enter `1` in the value field.
This ensures previous Manubot builds deploy before subsequent ones begin.

### CI clean up

The continuous integration configuration is now complete.
Clean up:

```sh
# Optionally remove untracked files
rm deploy.key*

# IMPORTANT: return to the repository's root directory
cd ..
```

## README updates

Now update `README.md` files to reference the new repository:

```sh
# Perform substitutions
sed "s/manubot\/rootstock/$OWNER\/$REPO/g" README.md > tmp && mv -f tmp README.md
sed "s/manubot\.github\.io\/rootstock/$OWNER\.github\.io\/$REPO/g" README.md > tmp && mv -f tmp README.md

# Remove deletable content file
git rm content/02.delete-me.md
```

## Finalize

Run `git status` or `git diff --color-words` to check that the following files have unstaged changes:

+ `README.md`

If the changes look okay, commit and push:

```sh
git add --update
git commit --message "Brand repo to $OWNER/$REPO"
git push origin master
```

You should be good to go now.
A good first step is to modify `content/metadata.yaml` with the relevant information for your manuscript.

# Merging upstream rootstock changes

This section will describe how to incorporate changes to rootstock that occurred since initializing your manuscript.
You will want to do this if there are new enhancements or bugfixes that you want to incorporate.
This process can be difficult, especially if conflicts have arisen, and is recommended only for advanced git users.

It is recommended to do rootstock upgrades via a pull request to help you view the proposed changes and to ensure the build uses the updated environment.
First, checkout a new branch to use as the pull request head branch:

```shell
# checkout a new branch, named using the current date, i.e. rootstock-2018-11-16
git checkout -b rootstock-$(date '+%Y-%m-%d')
```

Second, pull the new commits from rootstock, but do not automerge:

```shell
# if rootstock remote is not set, add it
git config remote.rootstock.url || git remote add rootstock https://github.com/manubot/rootstock.git

# pull the new commits from rootstock
git pull --no-ff --no-commit rootstock master
```

If all goes well, there won't be any conflicts.
However, if there are conflicts, follow the suggested commands to resolve them.

You can add the changes incrementally using `git add --patch`.
This is helpful to see each upstream change.
You may notice changes that affect how items in `content` are processed.
If so, you should edit and stage `content` files as needed.
When there are no longer any unstaged changes, then do `git commit`.

If updating `master` via a pull request, proceed to push the commit to GitHub and open a pull request.
Once the pull request is ready to merge, use GitHub's "Create a merge commit" option rather than "Squash and merge" or "Rebase and merge" to preserve the rootstock commit hashes.

The environment for local builds does not automatically update when [`build/environment.yml`](build/environment.yml) changes.
To update your local conda `manubot` environment with new changes, run:

```shell
# update a local conda environment
conda env update --file build/environment.yml
```

# Previewing pull request builds with AppVeyor

You can optionally enable AppVeyor continuous integration to view pull request builds.
Unlike Travis CI, AppVeyor supports storing manuscripts generated during pull request builds as artifacts.
These can be previewed to facilitate pull request review and ensure formatting and reference changes render as expected.
When a pull request build runs successfully, **@AppVeyorBot** will comment on the pull request with a download link to the manuscript PDF.

To enable AppVeyor, follow steps 1 and 2 of the [AppVeyor welcome](https://www.appveyor.com/docs/) to sign in to AppVeyor and add your manuscript repository as an AppVeyor project.
The repository already contains an `.appveyor.yml` build configuration file, so no other setup is required.
AppVeyor only runs when it detects changes that are likely to affect the manuscript.
