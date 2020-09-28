


def valid(string):
    """

    :param string: string to check if parenthesis is matching/valid
    :return: index, boolean (index=len(string) if True)

    """

    pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}

    stack = []
    for i in range(len(string)):

        char = string[i]
        print(stack, char)
        if char in pairs:
            stack.append(char)
        else:
            if len(stack) == 0:
                return i, False
            if char != pairs[stack[-1]]:
                return i, False
            stack.pop(-1)
    return max(0, i), True


if __name__ == '__main__':

    string = "((){[]})()"
    print(f'Input string: {string}')
    index, is_valid = valid(string)
    if is_valid:
        print("=> String is valid.")
    else:
        print(f"[ERROR] => string not valid (wrong at index {index})")