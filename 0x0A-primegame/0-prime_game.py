#!/usr/bin/python3
"""
module that defines the prime game
"""

def primeNumbers(n):
    """ generate a prime numbers list to n
    """
    primeN = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeN.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeN


def isWinner(x, nums):
    """ determine the winner"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeN = primeNumbers(nums[i])
        if len(primeN) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
