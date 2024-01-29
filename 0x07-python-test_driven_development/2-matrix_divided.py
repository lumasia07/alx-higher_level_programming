#!usr/bin/python3
"""

Module that divides all elements of a matrix

"""

def matrix_divided(matrix, div):
    """
    Defines function to divide all elements of a matrix
    """
    if not all(isinstance(i, list) and all(isinstance(x, (int, float))\
            for x in i) for i in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of\
                 integers/floats")
    if any(len(i) != len(matrix[0]) for i in matrix):
        raise TypeError("Each row of a matrix must have a same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(j / div, 2) for j in i] for i in matrix]

