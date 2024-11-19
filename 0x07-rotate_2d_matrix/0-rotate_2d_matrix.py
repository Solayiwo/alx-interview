#!/usr/bin/python3
"""Rotate 2D Matrix Module"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.
    :param matrix: List of lists representing the matrix.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):  # Start j from i+1 to avoid re-swapping
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # matrix[i][j] = matrix[j][i]
            # matrix[j][i] = matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
