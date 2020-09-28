
import math
import os


class Node:
    def __init__(self, value, d):
        self.left = None
        self.right = None
        self.value = value
        self.d = d

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


def build_tree(indexes):
    # Build tree
    nodes = {}
    root = Node(1, d=1)
    nodes[1] = root
    for i, (left, right) in enumerate(indexes, start=1):
        depth = math.floor(math.log2(i + 1)) + 1
        if i in nodes:
            if left != -1:
                node = Node(left, d=nodes[i].d+1)
                nodes[i].left = node
                nodes[left] = node
            if right != -1:
                node = Node(right, d=nodes[i].d+1)
                nodes[i].right = node
                nodes[right] = node
    return root, nodes


def swap_nodes(indexes, queries):
    if not indexes:
        return []
    res = []
    root, nodes = build_tree(indexes)
    # Invert nodes that are on depth given by queries
    for q in queries:
        for i, node in nodes.items():
            if node.d % q == 0:
                # invert(node)
                swap_children(node)
        res.append(in_order(root))

    return root, res


def in_order_recursive(root):
    res = []
    if root:
        res = in_order_recursive(root.left)
        res.append(root.value)
        res += in_order_recursive(root.right)
    return res


def in_order(root):
    res = []
    current = root
    stack = []
    done = 0
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif (stack):
            current = stack.pop()
            #print(current.data, end=" ")
            res.append(current.value)
            current = current.right
        else:
            break
    return res


def print_tree(root, space, count=5):
    if not root:
        return
    space += count

    print_tree(root.right, space)

    for i in range(count, space):
        print(" ", end='')
    print(f'{root.value}')

    print_tree(root.left, space)


if __name__ == '__main__':
    indexes = [[2, 3], [-1, -1], [-1, -1]]
    queries = [1, 1]
    root, _ = build_tree(indexes)
    print_tree(root, 0)                     # Print original tree
    print('-'*10 + '->')
    root, res = swap_nodes(indexes, queries)     # Swap nodes
    print_tree(root, 0)                     # Print new tree
    print(res)                   # Print in-order
    print('-' * 40)

    indexes = [[2, 3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]]
    queries = [2]
    root, _ = build_tree(indexes)
    print_tree(root, 0)                     # Print original tree
    print('-'*10 + '->')
    root, res = swap_nodes(indexes, queries)     # Swap nodes
    print_tree(root, 0)                     # Print new tree
    print(res)                   # Print in-order


    print('-' * 40)

    indexes = [[2,3],[4,-1],[5,-1],[6,-1],[7,8],[-1,9],[-1,-1],
               [10,11],[-1,-1],[-1,-1],[-1,-1]]
    queries = [2, 4]
    root, _ = build_tree(indexes)
    print_tree(root, 0)                     # Print original tree
    print('-'*10 + '->')
    root, res = swap_nodes(indexes, queries)     # Swap nodes
    print_tree(root, 0)                     # Print new tree
    print(res)                   # Print in-order

# if __name__ == '__main__':
#
#     with open('./test_cases/swap_nodes_tc10.txt', 'r') as fin:
#         n = int(fin.readline())
#         print(n)
#
#         indexes = []
#
#         for _ in range(n):
#             indexes.append(list(map(int, fin.readline().rstrip().split())))
#
#         queries_count = int(fin.readline())
#
#         queries = []
#
#         for _ in range(queries_count):
#             queries_item = int(fin.readline())
#             queries.append(queries_item)
#
#         print(indexes)
#         result = swap_nodes(indexes, queries)
#
#     with open('./test_cases/swap_nodes_tc10_out.txt', 'w') as fout:
#         fout.write('\n'.join([' '.join(map(str, x)) for x in result]))
#         fout.write('\n')

