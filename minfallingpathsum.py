from typing import List


def minFallingPathSum(A: List[List[int]]) -> int:

    for i in range(1, len(A)):
        for j in range(len(A[i])):
            min_elem = float('inf')
            for k in [-1, 0, 1]:
                if 0 <= (j + k) < len(A[i]):
                    min_elem = min(min_elem, A[i-1][j + k])
            A[i][j] += min_elem

    # print(A)
    return min(A[-1])


print(minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))