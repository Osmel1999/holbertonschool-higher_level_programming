#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2= [[i ** 2 for i in row] for row in matrix]
    return matrix_2
