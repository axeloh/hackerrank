"""
Given a list of numbers, find if there exists a pythagorean triplet
in that list.
A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

Example:
    Input: [3, 5, 12, 5, 13]
    Output: True
    (5^2 + 12^2 = 13^2)

"""


def pythagorean_triplets(nums):
    """
    Brute-force solution
    Time: O(n^2)
    Space: O(n)
    """
    nums = list(set(nums))  # To get rid of duplicates
    p_values = set([num**2 for num in nums])  # Store squared sums

    exist = False
    for i in range(len(nums)):
        base_num = nums[i]
        for j in range(i+1, len(nums)):
            p_sum = base_num**2 + nums[j]**2
            if p_sum in p_values:
                print(f'{base_num}^2 + {nums[j]}^2 = {int(p_sum**0.5)}^2 ')
                exist = True
                # return True
    if not exist:
        print('Found no triplets.')
    # return False


if __name__ == '__main__':
    lst = [3, 5, 12, 4, 13,]
    pythagorean_triplets(lst)
    print('-'*30)
    pythagorean_triplets(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
         14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
         25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40])




