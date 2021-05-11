
test_cases = int(input())


def trapping_rain_water(array):
    left_max = [0] * len(array)
    right_max = [0] * len(array)

    maxv = 0
    for i in range(len(array)):
        maxv = max(maxv, array[i])
        left_max[i] = maxv

    maxv = 0
    for i in range(len(array)-1 , -1, -1):
        maxv = max(maxv, array[i])
        right_max[i] = maxv

    total_val = 0
    for ind in range(len(array)):
        total_val += min(left_max[ind], right_max[ind]) - array[ind]

    return total_val


while test_cases:
    test_cases -= 1

    arr_size = int(input())
    arr = list(map(int, input().split(" ")))

    # print(arr)
    print(trapping_rain_water(arr))
