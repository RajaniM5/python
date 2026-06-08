#!/usr/bin/env python3
"""
Sample Python program with a `main()` function.
Usage:
  python3 main_program.py --name Rajani
"""

import argparse


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Greet a user")
    parser.add_argument("-n", "--name", default="world", help="Name to greet")
    args = parser.parse_args(argv)
    print(greet(args.name))


if __name__ == "__main__":
    main()
