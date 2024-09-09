#!/usr/bin/python3
"""Divide a matrix with a divisor."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)" 
                        " of integers/floats")
    len_0 = len(matrix[0])
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(matrix[i]) != len_0:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not (isinstance(matrix[i][j], int) or
                    isinstance(matrix[i][j], float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(row)
    return new_matrix
