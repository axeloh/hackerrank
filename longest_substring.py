"""
From leetcode.
Given a string, find the length of the longest substring without repeating characters.

"""


def lengthOfLongestSubstring(s: str) -> int:
    seen = set([])
    n = len(s)
    longest = 0
    longest_str = ""
    i = 0
    j = 0
    while i < n and j < n:
        c_j = s[j]
        # Try extend range [i, j]
        if not c_j in seen:
            seen.add(c_j)
            j += 1
            if j - i > longest:
                longest = j - i
                longest_str = s[i:j]

        else:
            c_i = s[i]
            seen.remove(c_i)
            i += 1

    return longest, longest_str


if __name__ == '__main__':
    string = "abcabcdefgbbb"
    print(string)
    longest, longest_str = lengthOfLongestSubstring(string)
    print('Longest substring is:')
    print(longest_str)
    print(f'with length: {longest}')