

"""
Dailyproblem from dailyinterviewpro.com

Given a list of numbers with only 3 unique numbers (1,2,3),
sort the list in O(n) time.

Example:
    Input: [3, 3, 2, 1, 3, 2, 1]
    Output: [1, 1, 2, 2, 3, 3, 3]

Challenge: Try sorting the list also using constant space
"""

# Loop over input arr
# store count of 1s 2s and 3s
# get count for 1s, insert count elements of 1s into array
# repeat step over for 2s and 3s


def sort(a):
    # Total: O(n) time, O(n) space

    count = {}
    # O(n) time, O(1) space
    for el in a:
        if el in count:
            count[el] += 1
        else:
            count[el] = 1

    # O(1) time, O(n) space
    sorted_a = []
    sorted_a.extend([1] * count[1])
    sorted_a.extend([2] * count[2])
    sorted_a.extend([3] * count[3])

    return sorted_a

# [3 3 2 1 3 2 1]
# [1 3 2 1 3 2 3]
# [1 2 3 1 3 3 3]
# [1 2 3 1 3 3 3]
# [1 2 1 3 3 3 3]
# [1 1 2 3 3 3 3]

# i = 2
# l = 2
# r = 3


def sort_inplace(a):
    # Time: O(n), Space: O(1)
    left_idx = 0
    right_idx = len(a) - 1
    i = 0
    while i <= right_idx:
        if a[i] == 1:
            if left_idx != i:
                a[i], a[left_idx] = a[left_idx], a[i]
            left_idx += 1
            i += 1
        elif a[i] == 2:
            i += 1
        elif a[i] == 3:
            a[i], a[right_idx] = a[right_idx], a[i]
            right_idx -= 1


if __name__ == '__main__':
    a = [3, 3, 2, 1, 3, 2, 1]
    sorted_a = sort(a)

    print(a)
    print('-'*20)
    print(sorted_a)

    sort_inplace(a)
    print(a)



