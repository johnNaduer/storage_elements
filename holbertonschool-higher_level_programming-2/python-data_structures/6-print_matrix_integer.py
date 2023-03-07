#!/usr/bin/python3
"""
def print_matrix_integer(matrix=[[]]):
    x = 0
    while x < len(matrix):
        y = 0
        while y < len(matrix[x]):
            print("{} ".format(matrix[x][y]), end="")
            y += 1
        print()
        x += 1
"""
def print_matrix_integer(matrix=[[]]):
    x = 0
    while x < len(matrix):
        y = 0
        while y < len(matrix[x]):
             print("{} ".format(matrix[x][y]), end="")
             y = y + 1
        print("")
        x = x + 1
