import argparse
import os
import pathlib
import shutil
import subprocess


def parse_arguments():
    """
    Read and process command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--checkout',
        nargs='?', const='gh-pages', default=None,
        help='branch to checkout /v directory contents from. For example, --checkout=upstream/gh-pages. --checkout is equivalent to --checkout=gh-pages. If --checkout is ommitted, no checkout is performed.',
    )
    parser.add_argument(
        '--version',
        default=os.environ.get('TRAVIS_COMMIT', 'local'),
        help="Used to create webpage/v/{version} directory. Generally a commit hash, tag, or 'local'",
    )
    args = parser.parse_args()
    return args


def configure_directories(args):
    """
    Add directories to args and create them if neccessary.
    Note that versions_directory is the parent of version_directory.
    """
    args_dict = vars(args)

    # Directory where Manubot outputs reside
    args_dict['output_directory'] = pathlib.Path('output')

    # Set webpage directory
    args_dict['webpage_directory'] = pathlib.Path('webpage')

    # Create webpage/v directory (if it doesn't already exist)
    args_dict['versions_directory'] = args.webpage_directory.joinpath('v')
    args.versions_directory.mkdir(exist_ok=True)

    # Checkout existing version directories
    checkout_existing_versions(args)

    # Create empty webpage/v/version directory
    version_directory = args.versions_directory.joinpath(args.version)
    if version_directory.is_dir():
        print(f'{version_directory} exists: replacing it with an empty directory')
        shutil.rmtree(version_directory)
    version_directory.mkdir()
    args_dict['version_directory'] = version_directory

    # Symlink webpage/v/latest to point to webpage/v/commit
    latest_directory = args.versions_directory.joinpath('latest')
    if latest_directory.is_symlink() or latest_directory.is_file():
        latest_directory.unlink()
    elif latest_directory.is_dir():
        shutil.rmtree(latest_directory)
    latest_directory.symlink_to(args.version, target_is_directory=True)
    args_dict['latest_directory'] = latest_directory

    # Create freeze directory
    freeze_directory = args.versions_directory.joinpath('freeze')
    freeze_directory.mkdir(exist_ok=True)
    args_dict['freeze_directory'] = freeze_directory

    return args


def checkout_existing_versions(args):
    """
    Must populate webpage/v from the gh-pages branch to get history

    References:
    http://clubmate.fi/git-checkout-file-or-directories-from-another-branch/
    https://stackoverflow.com/a/2668947/4651668
    https://stackoverflow.com/a/16493707/4651668

    Command modeled after:
    git --work-tree=webpage checkout upstream/gh-pages -- v
    """
    if not args.checkout:
        return
    command = [
        'git',
        f'--work-tree={args.webpage_directory}',
        'checkout',
        args.checkout,
        '--',
        'v',
    ]
    print('Attempting checkout with the following command:', ' '.join(command), sep='\n')
    process = subprocess.run(command, stderr=subprocess.PIPE)
    if process.returncode == 0:
        # Addresses an odd behavior where git checkout stages v/* files that don't actually exist
        subprocess.run(['git', 'add', 'v'])
    else:
        print(f'Checkout returned a nonzero exit status. See stderr:\n{process.stderr.decode()}')


def create_version(args):
    """
    Populate the version directory for a new version.
    """

    # Copy content/images to webpage/v/commit/images
    shutil.copytree(
        src=pathlib.Path('content/images'),
        dst=args.version_directory.joinpath('images'),
    )

    # Copy output files to to webpage/v/version/
    renamer = {
        'manuscript.html': 'index.html',
        'manuscript.pdf': 'manuscript.pdf',
    }
    for src, dst in renamer.items():
        shutil.copy2(
            src=args.output_directory.joinpath(src),
            dst=args.version_directory.joinpath(dst),
        )

    # Copy webpage/github-pandoc.css to to webpage/v/version/github-pandoc.css
    shutil.copy2(
        src=args.webpage_directory.joinpath('github-pandoc.css'),
        dst=args.version_directory.joinpath('github-pandoc.css'),
    )

    # Create v/freeze to redirect to v/commit
    path = pathlib.Path('build/assets/redirect-template.html')
    redirect_html = path.read_text()
    redirect_html = redirect_html.format(url=f'../{args.version}/')
    args.freeze_directory.joinpath('index.html').write_text(redirect_html)


def get_versions():
    """
    Extract versions from the webpage/v directory, which should each contain
    a manuscript.
    """
    versions = {x.name for x in args.versions_directory.iterdir() if x.is_dir()}
    versions -= {'freeze', 'latest'}
    versions = sorted(versions)
    return versions


if __name__ == '__main__':
    args = parse_arguments()
    configure_directories(args)
    print(args)
    create_version(args)
    versions = get_versions()
    print(versions)
