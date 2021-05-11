import collections
from typing import List
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    out = []

    c = collections.Counter(nums)
    curr = [(key, value) for key, value in c.items()]

    heapq.heapify(curr)

    while k:
        k -= 1
        out.append(heapq.heappop(curr)[0])

    return out


print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))
