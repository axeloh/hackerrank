
"""
Longest Common Substring Problem
Google Interview from https://www.youtube.com/watch?v=10WnvBk9sZc

Example:
"ABAZDC", "BACBAD" => "ABAD"

"""

#  i   0 1 2 3 4 5 6
#  j   Ø A B A Z D C
#  0 Ø 0 0 0 0 0 0 0
#  1 B 0 0 1 1 1 1 1
#  2 A 0 1 1 2 2 2 2
#  3 C 0 1 1 2 2 2 2
#  4 B 0 1 2 2 2 2 2
#  5 A 0 1 2 3 3 3 3
#  6 D 0 1 2 3 3 4 4

# res = 'ABAD'

# LCS function:
# Xi: substring of X (x1 x2 ... xi)
# Yj: substring of Y (y1 y2 ... yj)

# LCS(Xi, Yi) =
#    1) 0                                        if i = 0 or j = 0
#    2) LCS(X_i-1, Y_j-1) + 1                    if xi == yi
#    3) max[LCS(X_i-1, Y_j), LCS(X_i, Y_j-1)]    if xi != yi


def lcs(s1, s2):
    s1 = '_' + s1  # length m
    s2 = '_' + s2  # length n

    # Find the size of the longest common substring
    # time: O(mn)
    # space: O(mn)

    table = [[0 for _ in range(len(s1))] for _ in range(len(s2))]

    for i in range(1, len(s2)):
        for j in range(1, len(s1)):
            if s1[j] == s2[i]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    lcs_size = table[-1][-1]

    # If we only need length of lcs one can reduce the required space
    # Only need to store current and previous column
    # time: O(mn)
    # space: O(min(m,n))

    # Backtrack to find the longest common substring itself
    # O(max(m,n))
    lcs = ""
    i = len(table) - 1
    j = len(table[0]) - 1
    while i > 0 and j > 0:
        if s1[j] == s2[i]:
            lcs = s1[j] + lcs
            i -= 1
            j -= 1
        else:
            if table[i-1][j] > table[i][j-1]:
                i -= 1
            else:
                j -= 1

    return lcs_size, lcs


if __name__ == '__main__':
    s1 = "abcaddda"
    s2 = "abrrkadda"

    lcs_size, lcs = lcs(s1, s2)
    print(f'Found LCS of size={lcs_size}')
    print(f'LCS: {lcs}')
