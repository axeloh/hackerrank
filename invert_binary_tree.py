"""
You are given the root of a binary tree.
Invert the binary tree in place.
That is, all left children should become right children,
and all right children should become left children.
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def pre_order(self):
        print(self.value, end='\t')
        if self.left: self.left.pre_order()
        if self.right: self.right.pre_order()


def swap_children(node):
    if node.left and node.right:
        node.left, node.right = node.right, node.left
    elif node.left:
        node.right = node.left
        node.left = None
    else:
        node.left = node.right
        node.right = None


def invert(node):
    if node is None:
        return
    else:
        invert(node.left)
        invert(node.right)

    swap_children(node)

    return node


def print_tree(root, space, count=5):
    if root is None:
        return
    space += count

    print_tree(root.right, space)

    for i in range(count, space):
        print(" ", end='')
    print(f'{root.value}')

    print_tree(root.left, space)


if __name__ == '__main__':
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')
    root.right.right = Node('g')
    #root.left.left.left = Node('h')

    print_tree(root, 0)  # Original

    invert(root)  # Do inversion
    print('-'*50)

    print_tree(root, 0)  # Inverted
