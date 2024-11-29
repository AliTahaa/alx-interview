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
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
