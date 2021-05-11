def _01knapsack(wt: list, value: list, W: int, i=0) -> int:

    dp = dict()
    def return_dp(wt, value, W, i):
        if (i, W) in dp:
            return dp[(i, W)]

        if i >= len(wt):
            dp[(i, W)] = 0
            return 0

        if W == 0:
            dp[(i, W)] = 0
            return 0

        if wt[i] > W:
            dp[(i, W)] = return_dp(wt, value, W, i+1)
            return dp[(i, W)]

        dp[(i, W)] = max(value[i] + return_dp(wt, value, W-wt[i], i+1), return_dp(wt, value, W, i+1))
        return dp[(i, W)]

    return return_dp(wt, value, W, i)


print(_01knapsack([10, 20, 30], [60, 100, 120], 50))
