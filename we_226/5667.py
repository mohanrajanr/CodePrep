import collections
import math
from typing import List


def canEat(candiesCount: List[int], queries: List[List[int]]) -> List[bool]:

    prefix_count = [0]
    for count in candiesCount:
        prefix_count.append(prefix_count[-1] + count)

    answer = []
    for query in queries:

        favType = query[0]
        favDay = query[1]
        capacity = query[2]

        # # Starvation
        # if prefix_count[favType] + candiesCount[favType] < favDay:
        #     answer.append(False)
        #     continue
        #
        # # Excess
        # if prefix_count[favType] > capacity:
        #
        #     min_days_for_prefix = prefix_count[favType] // capacity
        #
        #     if min_days_for_prefix > favDay:
        #         answer.append(False)
        #         continue
        #
        #     remaining = prefix_count[favType] % capacity
        #
        # print(prefix_count[favType], candiesCount[favType])
        answer.append(prefix_count[favType] // capacity <= favDay < prefix_count[favType + 1])

    return answer


print(canEat([7,4,5,3,8], [[0,2,2],[4,2,4],[2,13,1000000000]]))
print(canEat([5,2,6,4,1], [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]))
