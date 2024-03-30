#!/usr/bin/python3
"""
descrition de  du module
"""


class Square:
    """ Classe Square """

    def __init__(self, f=0, position=(0, 0)):
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = position
        if type(f) is not int:
            raise TypeError("size must be an integer")
        elif f < 0:
            raise ValueError("size must be >= 0")
        elif type(f) is int:
            self.__size = f

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

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size + self.position[1]):
            if i < self.position[1]:
                pass
            else:
                for j in range(self.__size + self.position[0]):
                    if j < self.position[0]:
                        print("_", end="")
                    else:
                        print("#", end="")
            print()
