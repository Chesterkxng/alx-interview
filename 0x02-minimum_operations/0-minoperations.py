#!/usr/bin/python3
""" compute the min ops to achieve the task
return 0 if not possible
"""


def minOperations(n: int) -> int:
    """
    Minimum Operations
    """
    if n <= 0:
        return 0
    result: string = "H"
    tmp: string = ""
    num_operations: int = 0
    while len(result) < n:
        if n % len(result) == 0:
            tmp = result
            result += tmp
            num_operations += 2
            continue
        elif n % len(result) != 0:
            result += tmp
            num_operations += 1
            continue
    if len(result) == n:
        return num_operations
    return 0
