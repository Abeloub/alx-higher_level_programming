#!/usr/bin/python3
"""
The function takes a matrix and an integer, divides the matrix by the
int and returns the new matrix.
"""


def matrix_divided(matrix, div):
    """divide matrix by int div"""

    str_error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(str_error)
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(str_error)
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(str_error)
        row_count += 1
    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if not int(div):
        raise ZeroDivisionError("division by zero")
    new_matrix = list(
        map(lambda row: list(map(lambda x: round(x / div, 2), row)), matrix)
    )
    return new_matrix
