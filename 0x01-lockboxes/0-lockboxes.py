#!/usr/bin/python3
"""Define canUnlockAll function to unlock list of boxes"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list where each index represents a box
        and the values in the list represent keys that unlock other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    boxlen = len(boxes)

    if type(boxes) != list or boxlen == 0:
        return False

    unlocked = set([0])

    keys = set(boxes[0])

    while keys:
        key = keys.pop()

        if key < boxlen and key not in unlocked:
            unlocked.add(key)

            keys.update(boxes[key])

    return len(unlocked) == boxlen
