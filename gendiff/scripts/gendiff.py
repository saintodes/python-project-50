#!/usr/bin/env python3

import argparse
from gendiff.gendiff import generate_diff


def parce_cl():
    parser = argparse.ArgumentParser(
        description="Compares two configuration\
                                      files and shows a difference."
    )
    parser.add_argument("first_file", type=str, help="First file to compare")
    parser.add_argument("second_file", type=str, help="Second file to compare")
    parser.add_argument(
        "-f", "--format", type=str, nargs="?", default="stylish", help="Formatter select [stylish|plain|json], stylish is default"
    )
    args = parser.parse_args()
    return args


def main():
    args = parce_cl()
    difference = generate_diff(args.first_file, args.second_file, args.format)
    print(difference)


if __name__ == "__main__":
    main()
