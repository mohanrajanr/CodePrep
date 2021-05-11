from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:

    dp = [[0] * len(matrix[i]) for i in range(len(matrix))]

    maxval = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            dp[i][j] = int(matrix[i][j])
            maxval = max(maxval, dp[i][j])

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if dp[i][j] and dp[i-1][j] and dp[i-1][j-1] and dp[i][j-1]:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                maxval = max(maxval, dp[i][j])

    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         print(dp[i][j], end=" ")
    #     print('')

    return pow(maxval, 2)


print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(maximalSquare([["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]))
print(maximalSquare([["0","1"],["1","0"]]))