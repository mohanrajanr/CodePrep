from typing import List


def change(amount: int, coins: List[int]) -> int:

    dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
    dp[0][0] = 1
    for i in range(1, len(coins) + 1):
        dp[i][0] = 1
        for j in range(1, amount + 1):
            dp[i][j] = dp[i-1][j]
            if coins[i-1] <= j:
                dp[i][j] += dp[i][j - coins[i - 1]]

    return dp[len(coins)][amount]

print(change(5, [1, 2, 5]))
print(change(3, [2]))
print(change(10, [10]))