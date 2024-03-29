#!/usr/bin/python3
def uppercase(Fring:str):
    for u in Fring:
        print("{}".format(chr(ord(u)-32)), end="")
    print()
