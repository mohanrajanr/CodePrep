def romanToInt(s: str) -> int:
    mapping = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

    value = 0
    index = len(s)-1

    while index >= 0:

        st = s[index]

        if index > 0:
            if st == 'V' and s[index-1] == 'I':
                converted = 4
            elif st == 'X' and s[index-1] == 'I':
                converted = 9
            elif st == 'L' and s[index-1] == 'X':
                converted = 40
            elif st == 'C' and s[index-1] == 'X':
                converted = 90
            elif st == 'D' and s[index-1] == 'C':
                converted = 400
            elif st == 'M' and s[index-1] == 'C':
                converted = 900
            else:
                converted = mapping[st]
                index += 1
            # print(st, s[index-1], index, converted)
            index -= 1
        else:
            converted = mapping[st]
            # print(st, converted)

        value += converted
        index -= 1

    return value

# Test Case
test_cases = {"III": 3, "IV": 4, "IX": 9, "XIX": 19, "CM": 900, "XIV": 14}

for index, (input, output) in enumerate(test_cases.items(), 1):
    act_output = romanToInt(input)
    print(" ")
    print("Test Case:{} Validity:{}".format(index, act_output == output))
    print("Input:{} Expected:{} Act:{}".format(input, output, act_output))