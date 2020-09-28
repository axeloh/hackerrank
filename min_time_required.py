"""
You are planning production for an order.
You have a number of machines that each have a fixed number of days to
produce an item. Given that all the machines operate simultaneously,
determine the minimum number of days to produce the required order.

Example:
    machines = [2,3], goal = 5

    Day 1   2   3   4   5   6   7
    M0  0   1   0   1   0   1   0
    M1  0   0   1   0   0   1   0
Total   0   1   2   3   3   5   5
    => Takes six days to produce 5 items

"""

import math


def min_time_slowest(machines, goal, limit=1_000_000):
    """
    Iterates until goal is reached.
    let m = min(machines): the highest frequency
    Worst case only this machine will contribute
    Then we need m*goal days to produce goal items
    Each iteration loops over all n machines
    => Worst case time: O(goal*m*n)
    """
    day = 0
    #minimum = min(machines)
    while day < limit:
        produced = 0
        day += 1
        for m in machines:
            produced += day // m

        if produced >= goal:
            return day


def min_time_faster(machines, goal):
    """
    Uses a dict to store all machines with equal frequency
    This will speed it up quite a bit if this is the case for many machines
    """
    m_dict = {}
    for m in machines:
        if m in m_dict:
            m_dict[m] += 1
        else:
            m_dict[m] = 1

    day = 1
    while True:
        produced = 0
        for m in m_dict:
            produced += m_dict[m]*(day // m)
            #if day % m == 0:
            #    produced += 1
        if produced >= goal:
            return day
        day += 1


def get_produced(m_dict, day):
    produced = 0
    for m in m_dict:
        produced += m_dict[m] * (day // m)
    return produced


def min_time(machines, goal):
    m_dict = {}
    for m in machines:
        if m in m_dict:
            m_dict[m] += 1
        else:
            m_dict[m] = 1

    # Lower bound if all machines is as fast as the fastest
    lower_bound = math.ceil(goal * min(machines) / len(machines))

    # Upper bound if all machines is as slow as the slowest
    upper_bound = math.ceil(goal * max(machines) / len(machines))

    # Binary search within the bounds
    produced = None
    while lower_bound < upper_bound:
        day = (lower_bound + upper_bound) // 2
        produced = get_produced(m_dict, day)

        if produced < goal:
            lower_bound = day + 1
        elif produced >= goal:
            upper_bound = day

    # Check if same can be produced in less days
    while get_produced(m_dict, day - 1) == produced:
        day -= 1

    return int(lower_bound)


if __name__ == '__main__':
    ms, goal = [2, 3],  5
    print(min_time(ms, goal))  # 6
    print('-'*10)

    ms, goal = [2, 3, 2], 10
    print(min_time(ms, goal))  # 8
    print('-' * 10)

    ms, goal = [1, 3, 4], 10
    print(min_time(ms, goal))  # 7
    print('-' * 10)

    ms, goal = [4, 5, 6], 12
    print(min_time(ms, goal))  # 20
    print('-' * 10)

