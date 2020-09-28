"""
Question from "https://www.youtube.com/watch?v=pvimAM_SLic"

Given a random generator that generates random number uniformly in [0,1]:
Calculate the value of pi (!!).
"""

import random
import math

def isInCircle(x, y):
    # distance from origo
    return x**2 + y**2 <= 1

def estimate_pi(n):
    numInCircle = 0
    for _ in range(n):
        rndm_x = random.uniform(0, 1)
        rndm_y = random.uniform(0, 1)
        if isInCircle(rndm_x, rndm_y):
            numInCircle += 1

    # Area of square is 2*2 = 4
    # Area of circle is pi*r^2 = pi
    # => (A_circle / A_square) * A_square = pi
    # The relationship should be about equal in terms of # of points
    # in circle and square

    # numCircle / numSquare = A_circle/A_square
    # A_circle = (numCircle/numSqare)*A_square

    pi = 4 * numInCircle/n
    return pi


if __name__ == '__main__':
    n = 1000000
    pi = estimate_pi(n)
    print(pi)