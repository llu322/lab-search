"""Load text files and display results from your search helpers."""
import argparse
from pathlib import Path

from search import flatten_matches, group_matches, match_counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', help='Text to find, ignoring case')
    parser.add_argument('--folder', default='documents', help='Folder of UTF-8 .txt files')
    args = parser.parse_args()
    folder = Path(args.folder)
    if not folder.is_dir():
        parser.error(f'Folder does not exist: {folder}')
    paths = sorted(folder.glob('*.txt'))
    names = [path.name for path in paths]
    documents = [path.read_text(encoding='utf-8').splitlines() for path in paths]
    groups = group_matches(documents, args.query)
    for name, number, text in flatten_matches(names, groups):
        print(f'{name}:{number}: {text}')
    print('Matching lines per file:')
    for name, count in match_counts(names, groups).items():
        print(f'{name}: {count}')


if __name__ == '__main__':
    main()
