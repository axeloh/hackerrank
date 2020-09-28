"""
Daily question:
Given an array of integers,
find if it is possible to make the array non-decreasing by modifying at most 1 element

[13, 4, 7] -> True
[13, 4, 1] -> False

Find the solution in O(n) time.
"""


def check(lst):
    changeCount = 0
    if lst[0] > lst[1]:
        changeCount += 1
    lst[0] = lst[1]

    for i in range(1, len(lst)-1):
        el = lst[i]
        if lst[i] <= lst[i+1]:
            # All is good
            continue
        lst[i+1] = lst[i]
        changeCount += 1

    changeCount += 1 if lst[len(lst)-2] > lst[-1] else 0
    print(changeCount)
    return changeCount < 2


if __name__ == '__main__':
    # a = [13, 4, 1]
    a = [1, 2, 3, 4, 4, 4, 3, 3, 4, 5, 5]  # Should be false
    print(check(a))

    a = [13, 4, 1]  # Should be False
    print(check(a))

    a = [1, 2, 3, 4, 4, 4, 3, 4, 4, 5, 5]  # Should be True
    print(check(a))

    a = [9, 5, 2, 3, 4, 4, 4, 3, 4, 4, 5, 5]  # Should be False
    print(check(a))

