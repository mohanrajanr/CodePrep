def cbits(n):
    # for i in range(n):
    #     print("{} {}".format(i, bin(i).count("1")))
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    rec = 1
    for i in range(2, n+1):
        if rec * 2 == i:
            rec *= 2
        dp[i] = dp[i-rec] + 1

    return dp

print(cbits(9))