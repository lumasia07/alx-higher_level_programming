#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda a: list(map((lambda i: i ** i), a))), matrix))
