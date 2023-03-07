#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    x = 0
    while x < len(matrix):
        y = 0
        new_matrix2 = []
        while y < len(matrix[x]):
            n = matrix[x][y]**2
            new_matrix2.append(n)    
            y = y + 1
        new_matrix.append(new_matrix2)
        x = x + 1
    return (new_matrix)
