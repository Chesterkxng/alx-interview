#!/usr/bin/python3
'''Lockboxes.
'''
from collections import deque


def canUnlockAll(boxes):
    n = len(boxes)
    readed = set()
    queue = deque([0])

    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    while queue:
        curr = queue.popleft()
        readed.add(curr)

        for key in boxes[curr]:
            if key < n and key not in readed:
                queue.append(key)

    return len(readed) == n
