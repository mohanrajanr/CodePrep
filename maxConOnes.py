from collections import deque
from typing import List


def longestOnes(A: List[int], K: int) -> int:

    begin = 0
    end = 0

    while end < len(A):
        if K == 0:
            K += 1 - A[begin]
            begin += 1
        if not A[end]:
            K -= 1
        end += 1
        print(begin, end, K)

    return end - begin + 1

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(longestOnes([1,1,1,0,0,0,1,1,1,1], 0))
