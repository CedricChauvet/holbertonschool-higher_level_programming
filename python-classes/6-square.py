#!/usr/bin/python3
"""
descrition de  du module
"""


class Square:
    """ Classe Square """

    def __init__(self, f=0, position=(0, 0)):
        if type(f) is not int:
            raise TypeError("size must be an integer")
        elif f < 0:
            raise ValueError("size must be >= 0")
        elif type(f) is int:
            self.__size = f

        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, f):
        if type(f) is not int:
            raise TypeError("size must be an integer")
        elif f < 0:
            raise ValueError("size must be >= 0")
        elif type(f) is int:
            self.__size = f

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, p):
        if type(p) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(p) != 2 or:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(p[0]) is not int or type(p[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif p[0] < 0 or p[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = p            


    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
