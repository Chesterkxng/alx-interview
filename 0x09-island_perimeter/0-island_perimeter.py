#!/usr/bin/python3
"""
 function that computer perimeter of island
"""


def island_perimeter(grid):
    """ return the perimeter of island """
    m = len(grid)
    n = len(grid[0])
    perimeter = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
