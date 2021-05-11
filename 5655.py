from typing import List
import collections


def largestSubmatrix(matrix: List[List[int]]) -> int:

    rows = len(matrix)
    cols = len(matrix[0])

    col_ones = [[] for i in range(cols)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                col_ones[j].append(i)

    print(col_ones)

    return 0

print(largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))
print(largestSubmatrix([[1,0,1,0,1]]))
print(largestSubmatrix([[1,1,0],[1,0,1]]))
print(largestSubmatrix([[0,0],[0,0]]))