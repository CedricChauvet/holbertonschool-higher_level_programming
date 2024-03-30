#!/usr/bin/python3
"""
descrition de  du module
"""


class Square:
    """ Classe Square """

    def __init__(self, f=0, position=(0, 0)):
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
                print()
            else:
                for j in range(self.__size + self.position[0]):
                    if j < self.position[0]:
                        print("_", end="")
                    else:
                        print("#", end="")
            print()
