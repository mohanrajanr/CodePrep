def eatenApples(apples, days) -> int:

    max_days_valid = 0
    available_apples = 0
    num_of_apples = 0

    for supply, valid in zip(apples, days):

        max_days_valid = max(max_days_valid, valid)
        available_apples = min(max_days_valid, available_apples + supply)

        if available_apples > 0:
            num_of_apples += 1
            available_apples = max(available_apples -1, 0)

        max_days_valid = max(max_days_valid - 1, 0)

    return num_of_apples + available_apples

# Test Case
test_cases = [dict(input=dict(apples=[1,2,3,5,2], days=[3,2,1,4,2]), output=7),
              dict(input=dict(apples=[3,0,0,0,0,2], days=[3,0,0,0,0,2]), output=5),
              dict(input=dict(apples=[9,10,1,7,0,2,1,4,1,7,0,11,0,11,0,0,9,11,11,2,0,5,5], days=[3,19,1,14,0,4,1,8,2,7,0,13,0,13,0,0,2,2,13,1,0,3,7]), output=31),
              dict(input=dict(apples=[1,0,0,0,0,0,0,23], days=[7,0,0,0,0,0,0,1]), output=2),
              dict(input=dict(apples=[1,10, 17, 10, 12, 6, 20, 8, 8, 22, 14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,5,2,1,0,0,0,0,0,0,23], days=[19999,11, 18, 22, 5, 2, 14, 5, 20, 7, 17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,1,4,2,7,0,0,0,0,0,0,1]), output=2),
              dict(input=dict(apples=[1], days=[2]), output=1)]

for index, data in enumerate(test_cases, 1):
    act_output = eatenApples(**data['input'])
    print("Test Case:{} Validity:{}".format(index, act_output == data['output']))
    print("Input:{} Expected:{} Act:{}".format(data['input'], data['output'], act_output))
