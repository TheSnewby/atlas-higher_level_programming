#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(item, str) 
                                           for item in attrs):
            dict_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    dict_dict[key] = self.__dict__[key]
            return dict_dict

        return self.__dict__
