#!/usr/bin/python3
"""
MATRIX ROTATION
"""
from typing import List


def rotate_2d_matrix(matrix: List[int]):
    """    ROTATE 2D MATRIX
    """
    dict = {}
    n: int = len(matrix)
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
