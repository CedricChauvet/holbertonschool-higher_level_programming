#!/usr/bin/python3
def uppercase(Fring:str):
    
    for u in Fring:
        if ord(c) < 123 and ord(c) >= 97:
            print("{}".format(chr(ord(u)-32)), end="")
        else:
            print(u)            
