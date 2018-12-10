#!/usr/bin/env python3

import argparse
import contextlib
import json
import os
import sys

class BookmarkManager():
    def __init__(self, config_home):
        self._bookmarks_file = os.path.join(config_home, 'bookmarks')

        if not os.path.exists(self._bookmarks_file):
            with open(self._bookmarks_file, 'w') as bookmarks:
                json.dump({}, bookmarks, indent=4)
            self.reset()

    @contextlib.contextmanager
    def _auto_sync_marks(self):
        with open(self._bookmarks_file, 'r') as bookmarks:
            marks = json.load(bookmarks)
        yield marks
        with open(self._bookmarks_file, 'w') as bookmarks:
            json.dump(marks, bookmarks, indent=4, sort_keys=True)

    def query(self, mark):
        with self._auto_sync_marks() as marks:
            for this_mark, directory in marks.items():
                if mark == this_mark:
                    return directory
        return None

    def search(self, prefix):
        results = {}
        with self._auto_sync_marks() as marks:
            for mark, directory in marks.items():
                if not mark.startswith(prefix):
                    continue
                results[mark] = directory
        return results

    def reset(self):
        with self._auto_sync_marks() as marks:
            marks.clear()
            marks['.'] = '.'
            marks['..'] = '..'
            marks['-'] = '-'
            marks['home'] = os.environ['HOME']

    def add(self, mark, directory):
        with self._auto_sync_marks() as marks:
            marks[mark] = directory

    def delete(self, mark):
        try:
            with self._auto_sync_marks() as marks:
                del marks[mark]
            return True
        except KeyError:
            return False


def _get_config_dir():
    config_dir = os.path.join(os.environ['HOME'], '.config', 'goto-tool')
    os.makedirs(config_dir, exist_ok=True)
    return config_dir


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
    parser.add_argument(
        '--list-marks', dest='list', action='store_true',
        help='List all bookmarks')

    return parser.parse_args()


def _main():
    args = _parse_args()
    manager = BookmarkManager(_get_config_dir())

    if args.reset:
        manager.reset()
    elif args.query:
        mark = manager.query(*args.query)
        if mark is None:
            sys.exit('Mark not exist in bookmarks')
        print(mark, end='')
    elif args.search:
        marks = manager.search(*args.search)
        for mark in sorted(marks.keys()):
            print(mark)
    elif args.add:
        manager.add(*args.add)
    elif args.delete:
        if not manager.delete(*args.delete):
            sys.exit('Mark not exist in bookmarks')
    elif args.list:
        marks = manager.search('')
        for mark, directory in sorted(marks.items()):
            print('{:10s}  {:s}'.format(mark, directory))
    else:
        pass

    sys.exit()


if __name__ == '__main__':
    _main()
