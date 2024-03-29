#!/usr/bin/python3
def uppercase(Fring:str):
    
    for u in Fring:
        if ord(u) < 123 and ord(u) >= 97:
            k = (ord(u)-32)
        else:
            k = ord(u)
           
        print("{}".format(chr(k)), end='')
    print()
