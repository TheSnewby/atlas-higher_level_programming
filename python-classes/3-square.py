#!/usr/bin/python3
"""
Finds the area of a square
"""


class Square:
    """
    Creats a Square class with multiple options.
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise ValueError("size must be an integer")

    def area(self):
        """returns area of the square"""
        return self.__size ** 2
