#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda ligne: list(map(lambda col: col ** 2, ligne)), matrix))
