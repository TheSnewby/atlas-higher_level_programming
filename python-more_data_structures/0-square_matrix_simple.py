#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range (len(matrix[0]))]
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            new_matrix[x][y] = matrix[x][y] ** 2
    return new_matrix
