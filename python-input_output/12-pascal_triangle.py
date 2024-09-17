#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """creates a pascal's triangle n-levels tall"""
    if n <= 0:
        return []
    p = []
    for r in range(0, n): # r is row
        p.append([])
        for c in range(r+1): # c is column
            if c == 0:
                p[r].append(1)
            elif c == r:
                p[r].append(1)
            else:
                p[r].append(p[r - 1][c - 1] + p[r - 1][c])
    return p
