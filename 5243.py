import itertools
from typing import List
import collections


def tupleSameProduct(nums: List[int]) -> int:
    l = len(nums)
    if l < 4:
        return 0

    occur = 0
    res_set = collections.defaultdict(list)
    for i in range(l):
        for j in range(i+1, l):
            res_set[nums[i]*nums[j]].append((nums[i], nums[j]))

    for key, value in res_set.items():
        if key == 0 or len(value) < 2:
            continue

        occur += len(list(itertools.combinations(value, 2)))

    return occur * 8


print(tupleSameProduct([2,3,4,6]))
print(tupleSameProduct([1,2,4,5,10]))
print(tupleSameProduct([2,3,4,6,8,12]))
print(tupleSameProduct([2,3,5,7]))