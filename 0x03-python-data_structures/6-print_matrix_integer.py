#!/usr/bin/python3
def print_matrix_integer(matrix[[]]):
    for row in matrix:
        for column in range (len(row)):
            last = " " if column + 1 != len(row) else ""
            print("{:d}".format(row[column]), end=last)
        print()
