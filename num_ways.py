"""
You are given 2 integers n and m representing an n by m grid,
determine the number of ways you can get from
the top-left to the bottom-right of the matrix y going only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.


|  x |  x |  x |
|  x |  x |  x |
|  x |  x |  x |

"""

import time


def num_ways_recursive(n, m):
    # Recursive approach
    # O(2^nm) time
    # O(max(n,m)) space

    if n == 1 and m == 1:
        return 0
    if n == 1:
        return 1
    if m == 1:
        return 1

    return num_ways_recursive(n-1, m) + num_ways_recursive(n, m-1)


def num_ways(n, m):
    # Dynamic programming approach
    # O(nm) time
    # O(nm) space

    table = [[0 for _ in range(m)] for _ in range(n)]

    # Iteratively building rest of table
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                table[i][j] = 0
            elif i == 1 and j == 0:
                table[i][j] = 1
            elif i == 0 and j == 1:
                table[i][j] = 1
            else:
                table[i][j] = table[i-1][j] + table[i][j-1]

    # print('-'*30)
    # for row in table:
    #     print(row)

    return table[-1][-1]


if __name__ == '__main__':
    print(num_ways(2, 2))  # 2
    print(num_ways(4, 4))  # 20

    print(num_ways_recursive(2, 2))  # 2
    print(num_ways_recursive(4, 4))  # 20

    print('-'*30)

    # Compare time of the two approaches for high n
    n, m = 15, 15

    start = time.time()
    print(num_ways_recursive(n, m))
    end = time.time()
    print(f'Time using recursion: {(end - start):.4f}s')

    start = time.time()
    print(num_ways(n, m))
    end = time.time()
    print(f'Time using dynamic programming: {(end - start):.4f}s')

