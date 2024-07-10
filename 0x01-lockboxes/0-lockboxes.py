#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened.
    """
    if not boxes:
        return False

    unlocked = set([0])  # We can always open the first box
    keys = set(boxes[0])  # Keys we get from the first box

    while keys:
        key = keys.pop()
        if key not in unlocked and key < len(boxes):
            unlocked.add(key)
            keys.update(boxes[key])
            print(keys)

    return len(unlocked) == len(boxes)
