
def maximumBinaryString(binary: str) -> str:
    if '0' not in binary:
        return binary

    total = len(binary)
    corner_ones = binary.count("1", binary.find("0"))
    return '1' * (total - corner_ones - 1) + '0' + '1' * corner_ones


# Test Case
test_cases = {"000110": "111011", "01": "01"}

for index, (input, output) in enumerate(test_cases.items(), 1):
    act_output = maximumBinaryString(input)
    print("Test Case:{} Validity:{}".format(index, act_output == output))
    print("Input:{} Expected:{} Act:{}".format(input, output, act_output))
