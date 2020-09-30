# Table of contents

- [Creating a new manuscript](#creating-a-new-manuscript)
  * [Configuration](#configuration)
  * [Create repository](#create-repository)
  * [Continuous integration](#continuous-integration)
    + [GitHub Actions](#github-actions)
    + [SSH Deploy Key](#ssh-deploy-key)
      - [Add the public key to GitHub](#add-the-public-key-to-github)
      - [Add the private key to GitHub](#add-the-private-key-to-github)
    + [Travis CI](#travis-ci)
    + [Previewing pull request builds with AppVeyor](#previewing-pull-request-builds-with-appveyor)
  * [README updates](#readme-updates)
  * [Finalize](#finalize)
- [Merging upstream rootstock changes](#merging-upstream-rootstock-changes)

_generated with [markdown-toc](https://ecotrust-canada.github.io/markdown-toc/)_

# Creating a new manuscript

These instructions detail how to create a new manuscript based off of the [`manubot/rootstock`](https://github.com/manubot/rootstock/) repository.
The process can be a bit challenging, because it requires a few steps that are difficult to automate.
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
# GitHub username or organization name (change from manubot)
OWNER=manubot
# Repository name (change from rootstock)
REPO=rootstock
```

## Create repository

**Execute the remaining commands verbatim.**
They do not need to be edited (if the setup works as intended).

Next you must clone `manubot/rootstock` and reconfigure the remote repositories:

```sh
# Clone manubot/rootstock
git clone --single-branch https://github.com/manubot/rootstock.git $REPO
cd $REPO

# Configure remotes
git remote add rootstock https://github.com/manubot/rootstock.git

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
```

## Continuous integration

Manubot integrates with cloud services to perform continuous integration (CI).
For Manubot that means automatically building and deploying your manuscript.
Manubot supports the following CI services:

| Service | Default | Artifacts | Deployment | Config | Private Repos |
|---------|---------|-----------|---------|--------|---------------|
| [GitHub Actions](https://github.com/features/actions) | ✔️ | ✔️ | ✔️ | [`manubot.yaml`](.github/workflows/manubot.yaml) | 2,000 minutes per month |
| [Travis CI](https://travis-ci.com) | ❌ | ❌ | ✔️ needs setup | [`.travis.yml`](.travis.yml) | 100 build trial |
| [AppVeyor](https://www.appveyor.com/) | ❌ | ✔️ with PR comments | ❌ | [`.appveyor.yml`](.appveyor.yml) | 14 day trial |

Notes on table fields:

- **Default**: Whether the following uncollapsed setup instructions enable the service by default.
- **Artifacts**: Manuscript outputs that are saved alongside the CI build logs.
  This is especially helpful for previewing changes that are under development in a pull request.
  Both GitHub Actions and AppVeyor upload the rendered manuscript as an artifact for pull request builds.
  However, only AppVeyor comments on pull requests with a download link to the artifacts ([example](https://github.com/manubot/rootstock/pull/262#issuecomment-519944731)).
- **Deployment**: Whether the CI service can write outputs back to the GitHub repository (to the `output` and `gh-pages` branches).
  Deployment provides GitHub Pages with the latest manuscript version to serve to the manuscript's URL.
  GitHub Actions will deploy by default without any additional setup.
  Travis CI will only deploy if an SSH Private Key is provided.
  To avoid deploying a manuscript multiple times, disable GitHub Actions before providing an SSH Private Key to Travis.
- **Config**: File configuring what operations CI will perform.
  Removing this file is one method to disable the CI service.
- **Private Repos**: Quota for private repos.
  Only GitHub Actions supports cost-free builds of private repositories beyond a trial period.
  All services are cost-free for public repos.

### GitHub Actions

GitHub Actions is the recommended default CI service because it requires no additional setup.
To use GitHub Actions only, remove configuration files for other CI services:

```shell
# remove Travis CI config
git rm .travis.yml
# remove AppVeyor config
git rm .appveyor.yml
# remove ci/install.sh if using neither Travis CI nor AppVeyor
git rm ci/install.sh
```

GitHub Actions is _usually_ able to deploy without any additional setup using the [`GITHUB_TOKEN`](https://help.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token) for authentication.
GitHub Pages deployment using `GITHUB_TOKEN` recently started working on GitHub without an official announcement.
If it does not work for you after completing this setup, try reselecting "gh-pages branch" as the Source for GitHub Pages in the repository Settings.
GitHub Pages should now trigger on the next commit.
If not, [let us know](https://github.com/manubot/rootstock/issues/new).
For more reliable deployment on GitHub, you can also use an SSH Deploy Key instead (see below).

Deploying on Travis CI requires creating an SSH Deploy Key.
The following sections, collapsed by default, detail how to generate an SSH Deploy Key.

<details>
<summary>Expand for SSH Deploy Key setup</summary>

### SSH Deploy Key

Deployment on Travis CI requires an SSH Deploy Key.
Previously, GitHub Actions also required an SSH Deploy Key, but now GitHub can deploy using the `GITHUB_TOKEN` secret.
Therefore, users following the default configuration of deploying only via GitHub Actions can skip these steps.
Otherwise, generate a deploy key so CI can write to the repository.

```sh
# Generate deploy.key.pub (public) and deploy.key (private)
ssh-keygen \
  -t rsa -b 4096 -N "" \
  -C "deploy@manubot.org" \
  -f ci/deploy.key

# Encode deploy.key to remove newlines, writing encoded text to deploy.key.txt.
# This is required for entry into the Travis settings.
openssl base64 -A -in ci/deploy.key > ci/deploy.key.txt
```

#### Add the public key to GitHub

```sh
# Print the URL for adding the public key to GitHub
echo "https://github.com/$OWNER/$REPO/settings/keys/new"

# Print the public key for copy-pasting to GitHub
cat ci/deploy.key.pub
```

Go to the GitHub settings URL echoed above in a browser, and click "Add deploy key".
For "Title", add a description like "Manubot Deploy Key".
Copy-paste the contents of the `ci/deploy.key.pub` text file (printed above by `cat`) into the "Key" text box.
Check the "Allow write access" box below.
Finally, click "Add key".

#### Add the private key to GitHub

If you would like GitHub Actions to use SSH for deployment, rather than via HTTPS using `GITHUB_TOKEN`, perform the steps in this section.
**Skip this section if solely using Travis CI for deployment.**

```sh
# Print the URL for adding the private key to GitHub
echo "https://github.com/$OWNER/$REPO/settings/secrets"

# Print the encoded private key for copy-pasting to GitHub
cat ci/deploy.key.txt && echo
```

Next, go to the GitHub repository settings page (URL echoed above).
Click "Add a new secret".
For "Name", enter `MANUBOT_SSH_PRIVATE_KEY`.
Next, copy-paste the content of `ci/deploy.key.txt` into "Value"
(printed above by `cat`, including any trailing `=` characters if present).
</details>

<details>
<summary>Expand for Travis CI setup</summary>

### Travis CI

Travis CI is another option for continuous integration.
Now you must manually enable Travis CI for the new repository at <https://travis-ci.com>.
Click the `+` sign to "Add New Repository".
If you don't see your repository listed, push the "Sync account" button.
Finally, flick the repository's switch to enable CI.

```sh
# Print the URL for adding the private key to Travis CI
echo "https://travis-ci.com/$OWNER/$REPO/settings"

# Print the encoded private key for copy-pasting to Travis CI
cat ci/deploy.key.txt && echo
```

Next, go to the Travis CI repository settings page (URL echoed above).
Add a new record in the "Environment Variables" section.
For "NAME", enter `MANUBOT_SSH_PRIVATE_KEY`.
Next, copy-paste the content of `deploy.key.txt` into "VALUE"
(printed above by `cat`, including any trailing `=` characters if present).
Make sure "Display value in build logs" remains toggled off (the default).

While in the Travis CI settings, activate the [limit concurrent jobs](https://blog.travis-ci.com/2014-07-18-per-repository-concurrency-setting/) toggle and enter `1` in the value field.
This ensures previous Manubot builds deploy before subsequent ones begin.

Once the public and private deploy keys have been copied to their cloud locations, you can optionally remove the untracked files:

```sh
# Optionally remove untracked files
rm ci/deploy.key*
```

</details>

<details>
<summary>Expand for AppVeyor setup</summary>

### Previewing pull request builds with AppVeyor

You can optionally enable AppVeyor continuous integration to view pull request builds.
Unlike Travis CI, AppVeyor supports storing manuscripts generated during pull request builds as artifacts.
These can be previewed to facilitate pull request review and ensure formatting and reference changes render as expected.
When a pull request build runs successfully, **@AppVeyorBot** will comment on the pull request with a download link to the manuscript PDF.

To enable AppVeyor, follow steps 1 and 2 of the [AppVeyor welcome](https://www.appveyor.com/docs/) to sign in to AppVeyor and add your manuscript repository as an AppVeyor project.
The repository already contains an `.appveyor.yml` build configuration file, so no other setup is required.
AppVeyor only runs when it detects changes that are likely to affect the manuscript.
</details>

## README updates

The continuous integration configuration should now be complete.
Now update `README.md` files to reference your new repository:

```shell
# Perform substitutions
sed "s/manubot\/rootstock/$OWNER\/$REPO/g" README.md > tmp && mv -f tmp README.md
sed "s/manubot\.github\.io\/rootstock/$OWNER\.github\.io\/$REPO/g" README.md > tmp && mv -f tmp README.md
```

## Finalize

The `content/02.delete-me.md` file details the Markdown syntax and formatting options available with Manubot.
Remove it to reduce the content to a blank manuscript:

```shell
# Remove deletable content file
git rm content/02.delete-me.md
```

Run `git status` or `git diff --color-words` to double check the changes thus far.
If the changes look okay, commit and push:

```shell
git add --update
git commit --message "Brand repo to $OWNER/$REPO"
git push origin master
```

You should be good to go now.
A good first step is to modify [`content/metadata.yaml`](content/metadata.yaml) with the relevant information for your manuscript.

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
git pull --no-ff --no-rebase --no-commit rootstock master
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
