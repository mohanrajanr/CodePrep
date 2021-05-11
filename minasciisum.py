def minimumDeleteSum(s1: str, s2: str) -> int:

    total_sum = sum([ord(c) for c in s1])
    total_sum += sum([ord(c) for c in s2])

    dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            # print(s1[i-1], s2[j-1])
            if s1[i-1] == s2[j-1]:
                dp[i][j] = (ord(s1[i-1]) * 2) + dp[i-1][j-1]
                # print(s1[i-1], dp[i][j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return total_sum - dp[-1][-1]


print(minimumDeleteSum("sea", "eat"))
print(minimumDeleteSum("delete", "leet"))
