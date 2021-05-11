def halvesAreAlike(s: str) -> bool:
    def count_vows(st):
        return len([i for i in st if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']])

    mid = (len(s))//2
    return count_vows(s[:mid]) == count_vows(s[mid:])


# Test Case
test_cases = {"book": True, "textbook": False, "MerryChristmas": False, "AbCdEfGh": True}

for index, (input, output) in enumerate(test_cases.items(), 1):
    act_output = halvesAreAlike(input)
    print(" ")
    print("Test Case:{} Validity:{}".format(index, act_output == output))
    print("Input:{} Expected:{} Act:{}".format(input, output, act_output))
