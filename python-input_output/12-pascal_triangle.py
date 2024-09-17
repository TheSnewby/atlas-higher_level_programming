#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """creates a pascal's triangle n-levels tall"""
    if n <= 0:
        return []
    p = [[]]
    for r in range(1, n + 1): # r is row
        for c in range(r): # c is column
            p.append([])
            if c == 0:
                p[r].append(1)
            elif c == r - 1:
                p[r].append(1)
            else:
                p[r].append(p[r - 1][c - 1] + p[r - 1][c])
        print(p[r])
