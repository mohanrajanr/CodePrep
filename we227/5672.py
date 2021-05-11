from typing import List


def check(nums: List[int]) -> bool:
    difference = 0
    n = len(nums)
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            difference = i
            break

    for i in range(n - 1):
        if nums[(i + difference + 1) % n] < nums[(i + difference) % n]:
            print(nums[(i + difference + 1) % n], nums[(i + difference) % n], i, difference)
            return False
    return True


print(check([3, 4, 5, 1, 2]))
print(check([2, 1, 3, 4]))
print(check([1, 2, 3]))
print(check([1, 1, 1]))
print(check([2, 1]))
print(check([6, 10, 6]))