#!/usr/bin/python3
"""
descrition du module d'addition

"""


def add_integer(a: int, b=98):
    """
    fonction a implementer pour la rendre resistante
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if a == float('inf') or b == float('inf'):
        raise OverflowError("a or b is infinite")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a+b
