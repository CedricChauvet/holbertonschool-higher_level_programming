#!/usr/bin/python3
"""
descrition du module de division de matrice pas a number (int or float)
"""


def matrix_divided(matrix, div):
    """
    matrix dision:
    matrix made with int or float
    it s a mathematical matrix not a list of list
    div must be an int or a float
    div !=0
    return a new matrix, with 2 demal precision
    """
    indexcol = len(matrix)
    indexrow = len(matrix[0])
    
    for i in range(indexrow):
        if len(matrix[i]) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size") 
    
    
    
    
    
    matrixdiv = []
    for i in range(indexcol):
        matrixdiv.append([])
        for j in range(indexcol):
            matrixdiv[i].append(round(matrix[i][j]/div, 2))
    
    
    
    
    
    return matrixdiv
