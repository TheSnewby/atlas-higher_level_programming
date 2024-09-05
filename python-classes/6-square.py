#!/usr/bin/python3
"""Printing a square of a Square class"""


class Square:
    """creates a Square class with options"""
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        if (isinstance(position, tuple) and len(position) > 1
                and position[0] >= 0 and position[1] >= 0):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns area"""
        return self.__size ** 2

    @property
    def position(self):
        """returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """prints the square with #s in stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    if (i, j) == self.__position:
                        print(' ', end='')
                    else:
                        print('#', end='')
                print()
