#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_sorted = dict(sorted(a_dictionary.items()))
    for key, value in a_sorted.items():
        print('{}: {}'.format(key, value))
