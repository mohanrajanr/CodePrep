from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = [[]]
    for num in nums:
        res.extend([r + [num] for r in res])
    return res


print(subsets([1, 2, 3]))
print(subsets([0]))
