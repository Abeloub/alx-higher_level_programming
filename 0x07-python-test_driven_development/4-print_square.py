#!/usr/bin/python3
"""
The function takes a single integer argument and prints a square
with #s that has a length and width of size.
"""


def print_square(size):
    """prints a square with #s"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print("\n".join(["#" * size] * size), end="\n")
