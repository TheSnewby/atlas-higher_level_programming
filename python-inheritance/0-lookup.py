#!/usr/bin/python3
"""Lookup young padawan."""


def lookup(obj):
    """returns the list of available attributes and methods of an object."""
    if obj:
        return (dir(obj))
    return None
