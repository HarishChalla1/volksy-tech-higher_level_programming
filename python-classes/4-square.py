#!/usr/bin/python3
"""size of square"""


class Square:
    """A class that defines a square by size and can compute area"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(Self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, size):
        """size setter"""
        if type(size) !=int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """return area"""
        return self.__size**2
