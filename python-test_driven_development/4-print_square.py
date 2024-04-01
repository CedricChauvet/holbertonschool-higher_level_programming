#!/usr/bin/python3
"""
descrition du module 4 print square
"""


def print_square(size):
    """
    fonction qui ecrit des #
    """

    for i in range(size):
        print("")
        for j in range(size):
            print("#", end="")
    
    if size <0:
         raise Exception("size must be >= 0")
