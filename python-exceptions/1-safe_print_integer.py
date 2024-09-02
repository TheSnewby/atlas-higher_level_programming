#!/usr/bin/python3
def safe_print_integer(value):
    try:
        for num in value:
            try:
                print("{:d}".format(num))
            except ValueError:
                return False
    except TypeError:
        return False
    return True
