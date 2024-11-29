#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes

    Args:
        coins ([List]): List of Coins
        total ([int]): total amount
    """
    if total <= 0:
        return 0
    ch = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while ch < total:
            ch += i
            temp += 1
        if ch == total:
            return temp
        ch -= i
        temp -= 1
    return -1
