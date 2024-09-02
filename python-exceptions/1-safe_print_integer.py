#!/usr/bin/python3
def safe_print_integer(value):
    if isinstance(value, list) or isinstance(value, int):
        try:
            for num in value:
                print("{:d}".format(num))
        except ValueError:
            return False
        except TypeError:
            if isinstance(value, int):
                print("{:d}".format(value))
            else:
                return False
        return True
    return False
