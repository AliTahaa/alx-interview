#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n: int) -> int:
    """ Minimum Operations needed """
    n = 'H'
    b = 'H'
    o = 0
    while (len(b) < n):
        if n % len(b) == 0:
            o += 2
            n = b
            b += b
        else:
            o += 1
            b += n
    if len(b) != n:
        return 0
    return o
