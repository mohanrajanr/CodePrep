from typing import List


def kLengthApart(nums: List[int], k: int) -> bool:
    if k == 0:
        return True

    if not nums:
        return False

    first_1 = -1

    for i in range(len(nums)):
        if nums[i] == 1:
            first_1 = i
            break

    if first_1 == -1:
        return True

    for i in range(first_1+1, len(nums)):
        if nums[i] == 1:
            if i - first_1 - 1 < k:
                return False
            first_1 = i

    return True


print(kLengthApart([1,0,0,0,1,0,0,1], 2))
print(kLengthApart([1,0,0,1,0,1], 2))
print(kLengthApart([1,1,1,1,1,1], 0))
print(kLengthApart([0, 1, 0, 1], 1))
