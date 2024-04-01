#!/usr/bin/python3
"""
module numero 5 text indentation
"""


def text_indentation(text):
    """
    fonction numéro 5
    """
    charline = ""
    trig = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    
    for char in list(text):
        if char in [".","?",":"]:
            charline += char 
            charline+="\n\n"
            trig=2
        else:
            if trig >0 and char == " ":
                trig = trig - 1
            else:
                trig = trig - 1
                charline += char    
    print(charline,end="")
    