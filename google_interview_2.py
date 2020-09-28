"""
Google mock interview question from: https://www.youtube.com/watch?v=3Q_oYDQ2whs

"""

from functools import cmp_to_key
import time

def getHour(time, reverse=False):
    """
    :param time: string of format 9:30, 11:00, etc
    :return the hour
    """
    if reverse:
        return str(time[0])
    return int(time.split(':')[0])

def getMin(time, reverse=False):
    """
    :param time: string of format 9:30, 11:00, etc
    :return the minutes
    """
    if reverse:
        return str(time[1])
    return int(time.split(':')[1])

def asMin(time, reverse=False):
    """
    :param time: string of format 9:30, 11:00, etc
    :return the time in minutes from midnight (00:00)
    [630, 720]
    """
    if reverse:
        time = list(map(lambda t: [t//60, t%60], time))
        # [[9, 30], [10, 0]]
        return list(map(lambda t: f'{t[0]}:{0 if len(str(t[1])) == 1 else ""}{t[1]}', time))
    return 60*getHour(time) + getMin(time)



def getAvailableSlots(schedule, bound, duration):
    avail = []
    # find available spots in a schedule
    for i in range(len(schedule)):
        # time between current meeting end and next meeting start
        # First element
        if i == 0:
            start = bound[0]
            end = schedule[0][0]
        # Last element
        elif i == len(schedule) - 1:
            start = schedule[-1][1]
            end = bound[1]
        else:
            start = schedule[i][1]
            end = schedule[i + 1][0]

        # Append if enough time for this meeting
        time_avail = end - start

        if time_avail >= duration:
            avail.append([start, end])

    return avail


def getLatestTime(t1, t2):
    return t1 if compareTimesOrig(t1, t2) > -1 else t2

def compareTimesOrig(t1, t2):
    """t1 and t2 of the format '09:30' """
    h1, m1 = t1.split(':')
    h2, m2 = t2.split(':')
    t1 = int(h1) * 60 + int(m1)
    t2 = int(h2) * 60 + int(m2)

    if t1 < t2:
        return -1
    elif t1 > t2:
        return 1
    return 0

def compareTimes(t1, t2, useFinishTime=False):
    #h1, m1 = t1.split(':')
    #h2, m2 = t2.split(':')
    if useFinishTime:
        t1, t2 = t1[1], t2[1]
    else:
        t1, t2 = t1[0], t2[0]

    h1, m1 = t1.split(':')
    h2, m2 = t2.split(':')

    t1 = int(h1)*60 + int(m1)
    t2 = int(h2) * 60 + int(m2)

    if t1 < t2:
        return -1
    elif t1 > t2:
        return 1
    return 0



def availableMeetingTimes(a_schedule, b_schedule, a_bound, b_bound, duration):
    # a: length of a_schedule
    # b: length of b_schedule

    # O(1)
    a_bound = list(map(lambda m: asMin(m), a_bound))
    b_bound = list(map(lambda m: asMin(m), b_bound))

    # O(a+b)
    a_schedule = list(map(lambda m: [asMin(m[0]), asMin(m[1])], a_schedule))
    b_schedule = list(map(lambda m: [asMin(m[0]), asMin(m[1])], b_schedule))

    # O(1)
    a_schedule.insert(0, [0, a_bound[0]])
    b_schedule.insert(0, [0, b_bound[0]])
    a_schedule.append([a_bound[1], 24*60])
    b_schedule.append([b_bound[1], 24*60])

    res = []
    i = 0
    j = 0

    # Find the initial meeting to start comparing against
    a_start, a_end = a_schedule[i][0], a_schedule[i][1]
    b_start, b_end = b_schedule[j][0], b_schedule[j][1]
    if a_start <= b_start:
        current_end = a_end
        i += 1
    else:
        current_end = b_end
        j += 1

    # Iterating chronologically with respect to the starting time
    # O(a+b)
    while i < len(a_schedule) and j < len(b_schedule):
        if a_schedule[i][0] <= b_schedule[j][0]:
            next = a_schedule[i]
            i += 1
        else:
            next = b_schedule[j]
            j += 1

        next_start, next_end = next[0], next[1]
        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            gap = next_start - current_end
            if gap >= duration:
                res.append([current_end, next_start])
            current_end = next_end

    return res


if __name__ == '__main__':

    a_schedule = [['8:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
    a_bound = ['9:00', '20:00']

    b_schedule = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
    b_bound = ['10:00', '18:30']

    duration = 30 # in minutes

    # Should output : [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]

    # ------- Approach 1 -------

    start = time.time()
    # O(a+b)
    times = availableMeetingTimes(a_schedule, b_schedule, a_bound, b_bound, duration)

    print(f'Available slots for a meeting of {duration} minutes:')
    print([asMin(t, reverse=True) for t in times])
    print(f'Found in {(time.time() - start):.6f}s.')

    # ------- Alternative approach -------
    start = time.time()
    a_schedule.insert(0, ['00:00', a_bound[0]])
    b_schedule.insert(0, ['00:00', b_bound[0]])
    a_schedule.append([a_bound[1], '24:00'])
    b_schedule.append([b_bound[1], '24:00'])
    total = a_schedule + b_schedule

    # n = a + b
    # O(nlog n)
    total = sorted(total, key=cmp_to_key(compareTimes))

    res = []
    curr_end = '00:00'
    # O(n)
    while len(total) != 0:
        next = total.pop(0)
        if compareTimesOrig(next[0], curr_end) < 1:
            curr_end = getLatestTime(curr_end, next[1])
        else:
            gap = asMin(next[0]) - asMin(curr_end)
            if gap >= duration:
                res.append([curr_end, next[0]])
            curr_end = getLatestTime(curr_end, next[1])

    print('-'*60)
    print(f'Available slots for a meeting of {duration} minutes:')
    print(res)
    print(f'Found in {(time.time() - start):.6f}s.')

