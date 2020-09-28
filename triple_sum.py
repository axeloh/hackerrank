"""
Hackerrank problem.
Given 3 arrays a, b, c of different sizes, find the number of distinct
triplets (p, q, r) where p∈a, q∈b, r∈c,
satisfying the critera: p <= q and q >= r

Example:
    a = [3, 5, 7]
    b = [3, 6]
    c = [4, 6, 9]

    => Four triplets: (3,6,4), (3,6,6), (5,6,4), (5,6,6)

"""

import bisect


def triplets_slow(a, b, c):
    """
    Worst Case: O(n^3) time
    """
    a = sorted(a)
    b = sorted(b)
    c = sorted(c)

    triplets = set([])
    count = 0
    for index, q in enumerate(b):
        i, j = 0, 0
        while i < len(a):
            if a[i] <= q:
                while j < len(c):
                    if q < c[j]:
                        break
                    else:
                        #print(a[i], q, c[j])
                        if (a[i], q, c[j]) in triplets:
                            j += 1
                            continue
                        triplets.add((a[i], q, c[j]))
                        count += 1
                        j += 1
                i += 1
                j = 0
            else:
                break

    return count


def triplets(a, b, c):
    """
    m: # of elements in b
    n: # max of num elements in a and c
    Time: O(mlogn)
    Iterates over m elements in b | m times
    Binary search in a and c each time | each is O(logn) time
    Sorting in beginning is also O(nlogn)
    """

    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))

    count = 0
    for num in b:
        a_nums_less = bisect.bisect_right(a, num)
        c_nums_less = bisect.bisect_right(c, num)
        count += a_nums_less * c_nums_less

    return count


if __name__ == '__main__':

    a = [3, 5, 7]
    b = [3, 6]
    c = [4, 6, 9]
    count = triplets(a, b, c)
    print(count)  # Should be 4

    a = [1, 3, 5]
    b = [2, 3]
    c = [1, 2, 3]
    count = triplets(a, b, c)
    print(count)  # Should be 8

    a = [1, 3, 5, 7]
    b = [5, 7, 9]
    c = [7, 9, 11, 13]
    count = triplets(a, b, c)
    print(count)  # Should be 12

    a = [1, 4, 5]
    b = [2, 3, 3]
    c = [1, 2, 3]
    count = triplets(a, b, c)
    print(count)  # Should be 5
