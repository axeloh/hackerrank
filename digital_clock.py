"""
Microsoft Interview Question

Given four integers: A, B, C and D,
Find the maximum number of valid times (on a digital watch) that can be made

Example:
    2, 3, 3, 2 -> 3 valid times

22:33
23:23
23:32


abcd    0123
abdc    0132
acbd    0213
acdb    0231
adbc    0312
adcb    0321

"""


def isValidTime(a, b, c, d):
    return a in range(3) and b in range(10) and c in range(6) and d in range(10)

def validTimes(a, b, c, d):
    digits = [a, b, c, d]
    valid_first = sum(1 for i in set(digits) if i in range(3))
    valid_second = sum(1 for i in set(digits) if i in range(10))
    valid_third = sum(1 for i in set(digits) if i in range(6))
    valid_forth = sum(1 for i in set(digits) if i in range(10))

    print(valid_first)
    print(valid_second)
    print(valid_third)
    print(valid_forth)




if __name__ == '__main__':
    print(validTimes(1, 2, 3, 4))