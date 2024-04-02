#!/usr/bin/python3
"""
module numero 5 text indentation
"""


def text_indentation(text):
    """
    fonction numéro 5
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    new_text = text.replace(". ", ".")
    new_text = new_text.replace(": ", ":")
    new_text = new_text.replace("? ", "?")
    new_text = new_text.replace(".", ".\n\n")
    new_text = new_text.replace(":", ":\n\n")
    new_text = new_text.replace("?", "?\n\n")

    while(new_text.find("\n ") > 0):
        new_text = new_text.replace("\n ", "\n")    
    print(new_text, end="")
