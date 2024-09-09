#!/usr/bin/python3
"""Print square if you want to."""


def print_square(size):
    """prints a square with the character #"""
    if isinstance(size, int):
        if size >= 0:
            if not (size + 1 == size):
                for i in range(size):
                    for j in range(size):
                        print('#', end='')
                    print()
            else:
                raise ValueError("size is too large")
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
