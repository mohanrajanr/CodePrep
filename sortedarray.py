
def find_smallest(array):

    l = 1
    r = len(array)
    while l < r:
        m = l + (r - l)//2

        if array[m] > array[0]:
            l = m + 1
        else:
            r = m
        print(l, r, m)
    return l

# print(find_smallest([2, 3, 4, 5, 6, 7, 1]))


def find_max_inc_dec(array):
    # 2, 3, 4, 6, 4, 3, 2, 1 ( Increases and then decreases )

    l = 0
    r = len(array) + 1

    while l < r:
        m = l + (r - l) // 2

        if array[m] > array[m - 1]:
            l = m + 1
        else:
            r = m
        print(l, r, m)
    return l - 1

print(find_max_inc_dec([14, 13, 12, 11, 10]))