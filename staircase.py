
"""
You are given a positive integer N which represents the
number of steps in a staircase.
You can either climb 1 or 2 steps at a time.
Write a function that returns the number of unique ways to climb the stairs.

"""

import time


def staircase_recursive(n):
    """
    Recursive approach.
    Each function call calls itself twice until it reaches base case
    Takes O(n) 'levels' of calls until base case
    => Time: O(2^n)

    Will have a stack that fills up with calls in one path until that path
    reaches base case.
    Space complexity is proportional to the max depth of the recursion tree
    generated.
    => Space: O(n)
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    return staircase_recursive(n-1) + staircase_recursive(n-2)


def staircase(n):
    """
    Dynamic programming approach, bottom-up.
    Time: O(n)
    Space: O(n)
    """
    table = [0]*(n+1)
    # Base cases
    table[1] = 1
    table[2] = 2

    for i in range(3, n+1):
        table[i] = table[i-1] + table[i-2]

    return table[n]


if __name__ == '__main__':

    print(staircase_recursive(4))  # 5
    print(staircase_recursive(5))  # 8

    print(staircase(4))  # 5
    print(staircase(5))  # 8

    print('-'*30)
    # Compare time of the two approaches for high n
    n = 40

    start = time.time()
    print(staircase_recursive(n))
    end = time.time()
    print(f'Time using recursion: {(end - start):.4f}s')

    start = time.time()
    print(staircase(n))
    end = time.time()
    print(f'Time using dynamic programming: {(end - start):.4f}s')