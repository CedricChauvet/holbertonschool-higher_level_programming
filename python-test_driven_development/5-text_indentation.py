#!/usr/bin/python3
"""
module numero 5 text indentation
"""


def text_indentation(text):
    """
    fonction numéro 5
    """
    charline = ""
    trig = 2
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    
    for char in list(text):
        if char in [".","?",":"]:
            charline+="\n\n"
            trig=2
        else:
            if trig >0:
                trig = trig - 1
            else:
                charline += char    
    print(charline)
    