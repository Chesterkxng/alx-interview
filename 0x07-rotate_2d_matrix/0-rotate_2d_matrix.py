#!/usr/bin/python3
"""
MATRIX ROTATION
"""


def rotate_2d_matrix(matrix):
    """    ROTATE 2D MATRIX
    """
    dict = {}
    n = len(matrix)
    i = 0
    k = 0
    while i < n:
        row: List[int] = []
        for j in range(n - 1, -1, -1):
            row.append(matrix[j][k])
        dict[k] = row
        k = k + 1
        i = i + 1
    for key, val in dict.items():
        matrix[key] = val
