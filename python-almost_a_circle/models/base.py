#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Base Class for Rectangles and Squares"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer of Base instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts list of dictionaries to a json string"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """saves a list of dictionaries to a file"""
        Rectangle = __import__('rectangle').Rectangle
        if isinstance(cls, Rectangle):
            with open('Rectangle.json', 'w') as f:
                f.write(Base.to_json_string(list_objs))
        else:
            with open('Square.json', 'w') as f:
                f.write(Base.to_json_string(list_objs))

    def from_json_string(json_string):
        """unpacks a list of dictionaries from a json string"""
        if json_string is None:  # how to do if empty
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
        """creates new class instances from list of dictionaries"""
        Rectangle = __import__('rectangle').Rectangle
        Square = __import__('square').Square
        if isinstance(cls, Rectangle):
            new_rectangle = Rectangle(5, 6)
            new_rectangle.update(dictionary)
            return new_rectangle
        else:
            new_square = Square(5)
            new_square.update(dictionary)
            return new_square

    def load_from_file(cls):
        """loads a class instance from a file"""
        Rectangle = __import__('rectangle').Rectangle
        if cls is None:
            return []
        list_objs = []
        if isinstance(cls, Rectangle):
            with open('Rectangle.json', 'r') as f:
                loads = json.loads(f.read())
                for dict in loads:
                    list_objs.append(dict)
        else:
            with open('Square.json', 'r') as f:
                loads = json.loads(f.read())
                for dict in loads:
                    list_objs.append(dict)
        return list_objs
