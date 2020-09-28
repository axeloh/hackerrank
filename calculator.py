"""
Given a mathematical expression with just single digits, plus signs,
negative signs, and brackets, evaluate the expression.
Assume the expression is properly formed.

Example:
    Input: - ( 3 + ( 2 - 1 ) )
    Output: -4

"""


def is_valid(expr):
    if not expr:
        return -1, True

    pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}

    stack = []
    for i in range(len(expr)):
        char = expr[i]
        if char in pairs:
            stack.append(char)
        else:
            if len(stack) == 0:
                return i, False
            if char != pairs[stack[-1]]:
                return i, False
            stack.pop(-1)
    return max(0, i), True


def eval(expr):
    pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}
    signs = ['+', '-', '*', '/']

    # Extact parenthesis and check if valid
    wo_digits = ''.join([i for i in expr if i in pairs or i in pairs.values()])
    index, valid = is_valid(wo_digits)
    if not valid:
        print(f'Expression not valid. Error at index {index}.')
        return

    # Initialize stack and iterate over expression
    stack = [expr[0]]
    i = 1
    while i < len(expr):
        c = expr[i]

        if c == ' ':
            i += 1
            continue

        if c.isdigit() or c in pairs or c in signs:
            stack.append(c)

        # Else we have a closing parenthesis
        else:
            stack.append(c)
            print(f'start: {stack}')
            # Calculate sum within current parenthesis
            part_sum = 0

            # Pop until starting parenthesis and the preceding sign
            term = 0 # -1 2
            while c not in pairs:
                if not stack:
                    break
                c = stack.pop()
                if c.isdigit():
                    term += int(c)
                else:
                    if c == '-':
                        term *= -1
                    part_sum += term
                    term = 0

            # Check if a sign preceded the phrase
            if stack:
                c = stack.pop()
                if c == '-':
                    part_sum *= -1

            if part_sum <= 0:
                stack.append('-')
            else:
                stack.append('+')
            stack.append(str(abs(part_sum)))


            print(stack)
        i += 1

    print('-'*30)
    print(stack)
    # Now all parenthesis are gone
    # Just iterate through remaining stack to get total sum
    total = 0
    sign = 1
    for c in stack:
        if c.isdigit():
            total += sign * int(c)
        else:
            sign = -1 if c == '-' else 1

    return total


if __name__ == '__main__':
    # Should work with or without parenthesis and with spaces

    expr = "-(3+(2-3))"  # Should be -2
    res = eval(expr)
    print(f'sum: {res}')

    expr = "(-(3+(2-1)) - 5)"  # Should be -9
    res = eval(expr)
    print(f'sum: {res}')

    expr = "1+ 4 - 4"  # Should be 1
    res = eval(expr)
    print(f'sum: {res}')


# (-4 - 5)