#!/usr/bin/python3
"""
descrition du module 4 print square
"""


def print_square(size):
    """
    fonction qui ecrit des #
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
