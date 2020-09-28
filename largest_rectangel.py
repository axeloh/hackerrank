"""
There are a number of buildings in a certain two-dimensional landscape.
Each building has a height, given by h[i]
It should return an integer representing the largest rectangle
that can be formed within the bounds of consecutive buildings.

"""


def largest_rextangle2(lst):
    max_area = 0
    consecutive_heights = {}
    for i, height in enumerate(lst):
        for h in range(height + 1):
            if h in consecutive_heights:
                consecutive_heights[h] += 1
            else:
                consecutive_heights[h] = 1

            if h * consecutive_heights[h] > max_area:
                max_area = h * consecutive_heights[h]

        for h in consecutive_heights:
            if h > height:
                consecutive_heights[h] = 0

    return max_area


def largest_rectangle3(lst):
    stack = [[lst[0], 1]]
    height_count = {}
    max_area = lst[0]
    for i, h in enumerate(lst[1:], start=2):

        # print('-' * 20)
        # print(f'h count: {height_count}')
        # print(f'stack: {stack}')
        # print(f'max area: {max_area}')
        # print(f'h: {h}')
        #print(stack)
        prev_h, position = stack[-1]
        if h > prev_h:
            stack.append([h, i])

        else:
            while stack and prev_h >= h:
                stack.pop(-1)
                if not stack:
                    break
                prev_h, position = stack[-1]
                width = i - position
                area = width * prev_h
                if area > max_area:
                    max_area = area

            width = i - position
            area = width * h
            if area > max_area:
                max_area = area

            stack.append([h, position])

    print(stack)
    # print('-' * 20)
    # print(f'h count: {height_count}')
    # print(f'stack: {stack}')
    # print(f'max area: {max_area}')
    # print(f'h: {h}')
    # if stack:
    #     area = max([stack[i][0] * (len(lst) - stack[i][1]+1) for i in range(len(stack))])
    #
    #     if area > max_area:
    #         max_area = area

    return max_area


def largest_rectangle(h):
    s = []
    ans = len(h)
    h.append(0)

    for i in range(len(h)):
        left_index = i
        while len(s) > 0 and s[-1][0] >= h[i]:
            last = s.pop()
            left_index = last[1]
            ans = max(ans, h[i] * (i + 1 - last[1]))
            ans = max(ans, last[0] * (i - last[1]))
        s.append((h[i], left_index))

    return ans


if __name__ == '__main__':
    lst = [1, 3, 6, 8, 7, 2, 4, 1]  # 18
    print(largest_rectangle(lst))

    lst = [1, 2, 3, 4, 5]  # 9
    print(largest_rectangle(lst))

    lst = [8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116]
    print(largest_rectangle(lst))  # 26152

    lst = [11, 11, 10, 10, 10]
    print(largest_rectangle(lst))  # 50