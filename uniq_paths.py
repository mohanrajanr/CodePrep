# def uniquePaths(m: int, n: int) -> int:
#     dp = [[1 for j in range(n)] for i in range(m)]
#
#     for i in range(1, m):
#         for j in range(1, n):
#             dp[i][j] = dp[i-1][j] + dp[i][j - 1]
#
#     return dp[m-1][n-1]
#
# print(uniquePaths(3, 7))
# print(uniquePaths(3, 2))


# def uniquePathsWithObstacles(obstacleGrid: list) -> int:
#     m = len(obstacleGrid)
#     n = len(obstacleGrid[0])
#     dp = [[0 for j in range(n)] for i in range(m)]
#     dp[0][0] = 1 - obstacleGrid[0][0]
#     for i in range(1, m):
#         dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
#     for i in range(1, n):
#         dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])
#
#     for i in range(1, m):
#         for j in range(1, n):
#             dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) * (1 - obstacleGrid[i][j])
#
#     return dp[m - 1][n - 1]
#
#
# print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
# print(uniquePathsWithObstacles([[0,1],[0,0]]))


def minPathSum(grid) -> int:
    r = len(grid)
    c = len(grid[0])

    for i in range(1, r):
        grid[i][0] += grid[i - 1][0]

    for j in range(1, c):
        grid[0][j] += grid[0][j - 1]

    for i in range(1, r):
        for j in range(1, c):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[-1][-1]

# print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
# print(minPathSum([[1,2,3],[4,5,6]]))
print(minPathSum([[1,2],[1,1]]))
