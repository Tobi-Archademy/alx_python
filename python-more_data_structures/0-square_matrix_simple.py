#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[i**2 for i in elm] for elm in matrix]
    return new_matrix
