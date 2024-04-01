#!/usr/bin/python3
"""
descrition du module 4 print square
"""


def print_square(size):
    """
    fonction qui ecrit des #
    """

    if size <0:
        raise ValueError("size must be >= 0")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    

    for i in range(size):
        print("")
        for j in range(size):
            print("#", end="")
    
    