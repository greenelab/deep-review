import argparse
import pathlib
import random
import subprocess
import sys

import yaml
from manubot.util import read_serialized_data
from manubot.process.ci import get_continuous_integration_parameters


def parse_args():
    parser = argparse.ArgumentParser(
        description="Randomize metadata.authors. Overwrites metadata.yaml"
    )
    parser.add_argument(
        "--path", default="content/metadata.yaml", help="path to metadata.yaml"
    )
    parser.add_argument(
        "--shuffle",
        action="store_true",
        help="shuffle authors using HEAD commit as random seed",
    )
    parser.add_argument(
        "--only-on-ci",
        action="store_true",
        help="do nothing if CI environment variable is not true",
    )
    args = parser.parse_args()
    vars(args)["execute"] = True
    if args.only_on_ci:
        ci_params = get_continuous_integration_parameters()
        vars(args)["execute"] = bool(ci_params)
    return args


def shuffle(x, seed=None):
    """
    shuffle x in-place using seed
    """
    random.Random(seed).shuffle(x)


def get_head_commit():
    args = ["git", "rev-parse", "HEAD"]
    try:
        return subprocess.check_output(args)
    except subprocess.CalledProcessError:
        sys.stderr.write(f"randomize-authors: get_head_commit failed, setting seed to None.\n")
        return None


def dump_yaml(obj, path):
    path = pathlib.Path(path)
    sys.stderr.write(f"Dumping YAML to {path}\n")
    with path.open("w", encoding="utf-8") as write_file:
        yaml.dump(
            obj,
            write_file,
            # default_flow_style=False,
            explicit_start=True,
            explicit_end=True,
            width=float("inf"),
            sort_keys=False,
            allow_unicode=True,
        )
        write_file.write("\n")


if __name__ == "__main__":
    """
    Alternative to https://github.com/manubot/manubot/pull/214
    """
    args = parse_args()
    if not args.execute:
        sys.stderr.write("Exiting without doing anything due to --only-on-ci\n")
        sys.exit()
    metadata = read_serialized_data(args.path)
    authors = metadata.get("authors", [])
    if args.shuffle:
        sys.stderr.write("Shuffling metadata.authors\n")
        seed = get_head_commit()
        shuffle(authors, seed=seed)
    dump_yaml(metadata, args.path)
