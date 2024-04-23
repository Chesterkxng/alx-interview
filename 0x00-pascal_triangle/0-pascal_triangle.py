#!/usr/bin/python3
"""
module that definie Pascal Triangle
"""


def pascal_triangle(n):
    """ pascal triangle """
    if n <= 0:
        return []
    pt = [[1]]
    i = 0
    while i < n - 1:
        st = [1]
        j = 0
        while j < len(pt[i]) - 1:
            st.append(pt[i][j] + pt[i][j + 1])
            j += 1
        st.append(1)
        pt.append(st)
        i += 1
    return (pt)
