#!/usr/bin/python3
"""Base class"""


class Base:
    """Base Class for Rectangles and Squares"""
    __nb_ojects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_ojects
