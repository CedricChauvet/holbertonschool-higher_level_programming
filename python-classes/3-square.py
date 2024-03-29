#!/usr/bin/python3
"""
descrition de  du module
"""


class Square:
    """ Classe Square """

    def __init__(self, f=0):
        self.__size = self.ma_size(f)

    def ma_size(self, f):
        if type(f) is not int:
            raise TypeError("size must be an integer")
        elif f < 0:
            raise ValueError("size must be >= 0")
        elif type(f) is int:
            return f

    def area(self):
        return self.__size ** 2
