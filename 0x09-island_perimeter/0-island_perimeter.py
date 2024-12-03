#!/usr/bin/python3
"""
Defines the function island_perimeter to calculate the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a grid.

    Args:
        grid (list of list of int): A rectangular grid where:
            - 0 represents water.
            - 1 represents land.
            - Cells are connected horizontally/vertically (not diagonally).
            - The grid is surrounded by water.
            - The grid contains one island or nothing.
            - The island does not have internal "lakes" (enclosed water).

    Returns:
        int: The perimeter of the island in the grid.

    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
