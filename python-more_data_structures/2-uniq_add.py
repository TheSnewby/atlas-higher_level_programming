#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_values = set(my_list)
    sum = 0
    for value in uniq_values:
        sum += value
    return sum
