"""
Given two strings, determine the edit distance between them.
The edit distance is defined as the minimum number of edits
(insertion, deletion, or substitution)
needed to change one string to the other.

For example, "biting" and "sitting" have an edit distance of 2
(substitute b for s, and insert a t).

"""

def distance(s1, s2):
    i, j = len(s1)-1, len(s2)-1
    if i == -1:
        return j
    if j == -1:
        return i

    if s1[i] == s2[j]:
        return distance(s1[:i], s2[:j])
    else:
        return distance(s1, s2[:j]) + distance(s1[:i], s2)


if __name__ == '__main__':
    s1, s2 = "biting", 'sitting'
    print(distance(s1, s2))

