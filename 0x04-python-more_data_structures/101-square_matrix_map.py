#!/usr/bin/python3
def square_cal(n):
    return n ** 2
def square_matrix_map(matrix=[]):
    new_matrix = [map(square_cal, matrix)]
