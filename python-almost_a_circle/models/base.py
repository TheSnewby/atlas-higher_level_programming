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

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of dictionaries to a file"""
        filename = cls.__name__ + '.json'
        list_dicts = []
        if list_objs:
            for obj in list_objs:
                if obj is not None:
                    list_dicts.append(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(Base.to_json_string(list_dicts))

    def from_json_string(json_string):
        """unpacks a list of dictionaries from a json string"""
        if json_string in (None, ''):  # how to do if empty
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates new class instance from **dictionary"""
        if cls.__name__ == 'Rectangle':
            new_object = cls(1, 2)
        elif cls.__name__ == 'Square':
            new_object = cls(1)
        new_object.update(**dictionary)
        return new_object

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file"""
        if cls is None:
            return []
        list_objs = []
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                reading = f.read()
                loads = Base.from_json_string(reading)
                for dict in loads:
                    list_objs.append(cls.create(**dict))
        except FileNotFoundError:
            return []
        return list_objs
