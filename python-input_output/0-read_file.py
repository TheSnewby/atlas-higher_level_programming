#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """reads a text file and prints it to stdout"""
    with open(filename, 'r') as f:
        read_data = f.read()
        print(read_data, end='')
    f.closed
