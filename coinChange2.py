def coinChange(coins: list, amount: int) -> int:
    if amount == 0:
        return 0

    dp = dict()

    def back_track(amount_left, index):
        if (amount_left, index) in dp:
            # print("C", amount_left, index, dp[(amount_left, index)])
            return dp[(amount_left, index)]

        if amount_left < 0:
            return float('inf')

        if amount_left == 0:
            return 0

        if index >= len(coins):
            return float('inf')

        dp[(amount_left, index)] = min(back_track(amount_left - coins[index], index) + 1,
                                       back_track(amount_left - coins[index], index + 1) + 1,
                                       back_track(amount_left, index + 1)
                                       )
        # print(amount_left, index, dp[(amount_left, index)])
        return dp[(amount_left, index)]

    result = back_track(amount, 0)
    return result if result != float('inf') else -1

print(coinChange([1, 2, 5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([1], 1))
print(coinChange([1], 2))
