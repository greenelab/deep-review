import argparse
import re
import pathlib


inter_sentence_newline = re.compile(r'(?<=[a-zA-Z0-9,])\n(?=[[a-zA-Z0-9])')


def reflow(text):
    """
    Remove newlines that are likely inserted from wordwrapping in markdown
    documents.
    """
    text = inter_sentence_newline.sub(' ', text)
    return text


if __name__ == "__main__":
    """
    Run like
    $ python build/remove-newlines.py --in-place content/0[2-8]*.md
    
    For more extensive solutions and discussion, see:
    + https://stackoverflow.com/questions/4576077
    + https://github.com/greenelab/deep-review/issues/624
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='+', type=pathlib.Path)
    parser.add_argument('--in-place', action='store_true')
    args = parser.parse_args()
    for path in args.paths:
        print(f'Reflowing {path}')
        text = path.read_text()
        text = reflow(text)
        if args.in_place:
            path.write_text(text)
        else:
            print(text)
