#!/usr/bin/python3
"""
descrition du module de division de matrice pas a number (int or float)
"""


def matrix_divided(matrix, div):
    indexcol = len(matrix)
    indexrow = len(matrix[0])
    matrixdiv = []
    for i in range(indexcol):
        matrixdiv.append([])
        for j in range(indexcol):
            matrixdiv[i].append(round(matrix[i][j]/div, 2))
    return matrixdiv
