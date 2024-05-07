#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n: int) -> int:
    """
    min ops
    """
    if (not isinstance(n, int) or n <= 1):
        return 0
    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op
