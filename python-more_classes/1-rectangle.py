#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """Width & Height"""
    def __init__(self, width=0, height=0):
        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
    def width(self):
        """retrieves width"""
        return self.__width
    def height(self):
        """retrieves height"""
        return self.__height
    def width(self, width):
        """setter for width"""
        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
    def height(self, height):
        """setter for height"""
        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
