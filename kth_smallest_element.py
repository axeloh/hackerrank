

"""
Find the k-th smallest number in an array
"""

import bisect
import random


def kth_smallest(arr, k):
    # O(nlogk)
    arr = list(set(arr))
    temp = [1e8 for _ in range(k)]
    for i in range(len(arr)):
        if arr[i] < temp[k-1]:
            bisect.insort(temp, arr[i])
    return temp[k-1]

def kth_smallest_qs(arr, k):
    if k == 1:
        return min(arr)
    if k == len(arr):
        return max(arr)
    # Quick select
    # Average O(n), Worst case O(n^2)
    arr = list(set(arr))
    idx = random.randrange(len(arr)-1)
    pivot = arr[idx]
    smaller = []
    bigger = []
    for i in range(len(arr)):
        if arr[i] < pivot:
            smaller.append(arr[i])
        else:
            bigger.append(arr[i])

    # print('-'*30)
    # print(arr)
    # print(f'k: {k}')
    # print(f'pivot: {pivot}')
    # print(f'smaller: {smaller}')
    # print(f'bigger: {bigger}')

    if len(smaller) > k - 1:
        return kth_smallest_qs(smaller, k)
    elif len(smaller) < k - 1:
        return kth_smallest_qs(bigger, k-len(smaller))

    return pivot

if __name__ == '__main__':
    arr = [3, 100, -1, 5, 9, 7, -1, 2]
    k = random.randrange(1, len(arr))
    print(f'k: {k}')

    res = kth_smallest(arr, k)
    print(res)

    res = kth_smallest_qs(arr, k)
    print(res)

