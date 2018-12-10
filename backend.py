#!/usr/bin/env python3

import argparse

class BookmarkManager():
    def __init__(self):
        pass

    def query(self, mark):
        pass

    def search(self, prefix):
        pass

    def reset(self):
        pass

    def add(self, mark, directory):
        pass

    def delete(self, mark):
        pass


def _parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--reset-marks', dest='reset', action='store_true',
        help='reset bookmark storage')
    parser.add_argument(
        '--query-directory', dest='query', nargs=1, metavar='bookmark',
        help='Query directory by given bookmark')
    parser.add_argument(
        '--search-marks', dest='search', nargs=1, metavar='prefix',
        help='Search bookmarks by prefix')
    parser.add_argument(
        '--add-mark', dest='add', nargs=2, metavar=('bookmark', 'directory'),
        help='Add bookmark with specified directory')
    parser.add_argument(
        '--delete-mark', dest='delete', nargs=1, metavar='bookmark',
        help='Delete given bookmark')

    return parser.parse_args()


def _main():
    args = _parse_args()
    manager = BookmarkManager()

    if args.reset:
        manager.reset()
    elif args.query:
        manager.search(*args.query)
    elif args.search:
        manager.search(*args.search)
    elif args.add:
        manager.add(*args.add)
    elif args.delete:
        manager.delete(*args.delete)
    else:
        pass


if __name__ == '__main__':
    _main()
