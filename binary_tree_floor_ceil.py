
"""
Given an integer k and a binary search tree, find the floor (less than or equal to) of k,
and the ceiling (larger than or equal to) of k.
If either does not exist, then print them as None.

"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root, k, floor=None, ceil=None):
    # Find floor
    node = root
    while node is not None:
        if node.value == k:
            floor = node.value
            break
        elif k < node.value:
            node = node.left
        else:
            floor = node.value
            node = node.right

    # Find ceiling
    node = root
    while node is not None:
        if node.value == k:
            ceil = node.value
            break
        elif k > node.value:
            node = node.right
        else:
            ceil = node.value
            node = node.left

    return floor, ceil


if __name__ == '__main__':
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.left = Node(10)
    root.right.right = Node(14)

    print(findCeilingFloor(root, 8))
    # (4, 6)

    print(findCeilingFloor(root, 1))
    # (None, 2)
