"""
You are given a 2D array of characters, and a target string.
Return whether or not the word target word exists in the matrix.
Unlike a standard word search, the word must be either going
left-to-right, or top-to-bottom in the matrix.

"""

import numpy as np


def word_search(m, word):
    # 'hack'-solution using numpy
    m = np.array(m)

    for i in range(len(m)):
        row = m[i, :]
        if word in ''.join(row):
            return True

    for j in range(len(m[0])):
        col = m[:, j]
        if word in ''.join(col):
            return True

    return False


if __name__ == '__main__':
    matrix = [['F', 'A', 'C', 'I'],
              ['O', 'B', 'Q', 'P'],
              ['A', 'N', 'O', 'B'],
              ['M', 'A', 'S', 'S']]
    print(word_search(matrix, 'FOAM'))  # True


