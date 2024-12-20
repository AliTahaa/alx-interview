#!/usr/bin/python3
""" lockboxes problem """


def canUnlockAll(boxes):
    """ Determines whether a series of locked boxes can be opened """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_check = False
        for idx in range(len(boxes)):
            boxes_check = k in boxes[idx] and k != idx
            if boxes_check:
                break
        if boxes_check is False:
            return boxes_check
    return True
