#!/usr/bin/python3
"""
This module creates a square with size.
"""


class Square:
    """
    Square class with private size.
    """
    def __init__(self, size):
        self.size = size
        self.__size = size
