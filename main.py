#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from kernel import LIBRARIES
import sys

def main():
    parser = argparse.ArgumentParser(description='Create and test re-usable tools')
    subparsers = parser.add_subparsers()

    for library_key, library in LIBRARIES.items():
        library_group = subparsers.add_parser(library_key, description=library.description())
        library_subparsers = library_group.add_subparsers()

        for command, operation in library.operations().items():
            operation_subparser = library_subparsers.add_parser(command, description=operation.description())
            operation.parser(operation_subparser)
            operation_subparser.set_defaults(function=operation.execute)

    try:
        results, unknown_args = parser.parse_known_args()
        results.function(results,unknown_args)
    except AttributeError:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()