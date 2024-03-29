#!/usr/bin/python3
def uppercase(Fring:str):
    
    for u in Fring:
        if ord(u) < 123 and ord(u) >= 97:
            print("{}".format(chr(ord(u)-32)), end="")
        else:
            print(u, end="")            

