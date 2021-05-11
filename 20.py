def isValid(s: str) -> bool:
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    index = 0
    while index < len(s):

        val = s[index]

        if val in brackets.keys() and len(stack) > 0:
            popped = stack.pop()
            for value in brackets.keys():
                if val == value and popped != brackets[value]:
                    return False
        elif val in brackets.values():
            stack.append(val)
        else:
            return False

        index += 1

    return True if len(stack) == 0 else False

# Test Case
test_cases = {"()": True, "{[]}": True, "([)]": False, "(]": False, "(){}[]": True}

for index, (input, output) in enumerate(test_cases.items(), 1):
    act_output = isValid(input)
    print(" ")
    print("Test Case:{} Validity:{}".format(index, act_output == output))
    print("Input:{} Expected:{} Act:{}".format(input, output, act_output))