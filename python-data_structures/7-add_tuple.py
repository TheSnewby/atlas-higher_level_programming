#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    if a_len > 0:
        first = tuple_a[0]
    else:
        first = 0
    if b_len > 0:
        first += tuple_b[0]

    if a_len > 1:
        second = tuple_a[1]
    else:
        second = 0
    if b_len > 1:
        second += tuple_b[1]
    return (first, second)
