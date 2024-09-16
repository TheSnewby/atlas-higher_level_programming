#!/usr/bin/python3
"""write to a file"""


def write_file(filename='', text=''):
    """writes a string to a textfile and returns the num of chars written"""
    with open(filename, 'w+') as f:
        f.write(text)
