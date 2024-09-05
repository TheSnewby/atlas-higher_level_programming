#!/usr/bin/python3
"""
This module performs size validation on a Square class.
"""


class Square:
    """
    Class that creates a square with options.
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
