#!/usr/bin/python3
"""
descrition du module say my name
"""


def say_my_name(first_name, last_name=""):
    """ Affiche une ligne de texte"""

    if type(first_name) is not str:
        raise Exception("first_name must be a string")

    if type(last_name) is not str:
        raise Exception("last_name must be a string")
    print("My name is", first_name, last_name)
