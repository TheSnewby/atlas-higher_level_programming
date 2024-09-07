#!/usr/bin/python3
"""How many instances of a Rectangle"""


class Rectangle:
    """Width & Height"""
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = '#'

    @property
    def width(self):
        """retrieves width"""
        return self.__width

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @width.setter
    def width(self, width):
        """setter for width"""
        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, height):
        """setter for height"""
        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter"""
        if self.__width > 0 and self.__height > 0:
            return self.__width * 2 + self.__height * 2
        else:
            return 0

    def __str__(self):
        if self.__width > 0 and self.__height > 0:
            string = ''
            for h in range(self.__height):
                for w in range(self.__width):
                    string += self.print_symbol
                if h != self.__height - 1:
                    string += '\n'
            return string
        else:
            return ''

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)


    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

