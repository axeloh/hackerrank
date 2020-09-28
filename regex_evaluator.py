"""
Google Interview from https://www.youtube.com/watch?v=tj_sBZw9nS0
Write a function that takes two trings as arguments, s and p,
and returns a boolean denoting whether s matches p

p is a sequence of any number of the following:
1) a-z : which stands for itself
2) . : which matches any character
3) * : which matcher 0 or more occurences of the previous singe character

Examples:
    s = "aba", p = "ab" => False
    s = "aa", p = "a*" => True
    s = "ab", p = ".*" => True
    s = "ab", p = "." => False
    s = "aab", p = "c*a*b*" => True
    s = "aaa", p = "a*." => True
"""


def match(s, p):
    j = 0  # index for p
    i = 0  # index for s
    prev = ''
    while i < len(s):
        if j >= len(p):
            return False
        print('-'*15)
        print(s[i])
        print(p[j])
        char = s[i]
        pj = p[j]
        if pj == '.':
            prev = '.'
            i += 1
            j += 1
        elif pj == '*':
            if char == prev or prev == '.':
                if i+1 < len(s) and j+1 < len(p):
                    if s[i+1] == p[j+1] or p[j+1] == '.':
                        j += 1
            i += 1
        else:
            prev = char
            if char != pj:
                if j + 1 < len(p) and p[j+1] == '*' :
                    j += 1
                else:
                    return False
            else:
                i += 1
            j += 1

    print(j)
    print(p[j:])
    if j < len(p) and p[-1] != '*':
        return False
    return True


if __name__ == '__main__':
    s = "abb"
    p = "abba"
    match = match(s, p)
    print(match)

"""
s = "aba", p = "ab" => False
    s = "aa", p = "a*" => True
    s = "ab", p = ".*" => True
    s = "ab", p = "." => False
    s = "aab", p = "c*a*b*" => True
    s = "aaa", p = "a*." => True


prev = ''

loop over chars in s:
    if p == '.':
        prev = '.'
        continue
    elif p == '*':
        check if char == prev or prev == '.'
        If yes => next char but same p
        If no => same char but next p
        
    else: (p == [a-z])
        if next_char == '*':
            prev = char
            continue
        else:
            check whether char == p
            If yes => continue
            If f no => return False
        
"""

