#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """returns if True if the object is exactly an instance of the
    specified class, otherwise returns False."""
    if isinstance(a_class, type) and type(obj) is a_class:
        return True
    return False
