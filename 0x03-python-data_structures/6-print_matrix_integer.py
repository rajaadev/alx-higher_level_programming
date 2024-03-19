#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not in matrix:
        return None
    for list_row in matrix:
        for i in range(len(list_row)):
            print("{:d}".format(list_row[i]), end="")
            if i != len(list_row) - 1:
                print(" ", end="")
        print()
