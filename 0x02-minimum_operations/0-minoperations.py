#!/usr/bin/python3
""" Script that computes a minimum operations """


def minOperations(n):
    """ Method for compute the minimum number of tasks """
    if n < 2:
        return 0
    f_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                f_list.append(i)
    return sum(f_list)
