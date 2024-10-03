#!/usr/bin/python3
"""A function hat returns a list of lists o
   integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    """First row is always [1]"""
    triangle = [[1]]

    for i in range(1, n):
        """Start with 1"""
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        """Add row to triangle"""
        triangle.append(row)

    return triangle
