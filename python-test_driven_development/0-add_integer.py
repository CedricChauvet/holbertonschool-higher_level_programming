#!/usr/bin/python3
"""
descrition du modume d'addition
"""


def add_integer(a: int, b=98):
    """
    fonction a implementer pour la rendre resistante
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if a is float:
        a = int(a)
    if b is float:
        b = int(b)
    return a+b
