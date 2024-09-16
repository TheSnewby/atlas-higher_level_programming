#!/usr/bin/python3
"""Append to a file"""


def append_write(filename='', text=''):
    """appends a string at the end of a text file and returns chars added"""
    with open(filename, 'a') as f:
        chars_added = f.write(text)
    return chars_added
