#!/usr/bin/python3
"""A module for lock picking.
"""


def canUnlockAll(boxes):
    """Check if all boxes can be unlocked.
    """
    n = len(boxes)
    seen_boxes = {0}
    unseen_boxes = set(boxes[0]).difference({0})
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
