#!/usr/bin/python3
"""My list of lists."""


class MyList(list):
    """Class inherits from list."""
    def print_sorted(self):
        """prints a sorted (ascending) list.
        """
        print(sorted(self))
