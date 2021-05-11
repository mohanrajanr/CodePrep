def lcs(s1, s2) -> int:
    dp = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]

    # for i in range(len(s1) + 1):
    #     for j in range(len(s2) + 1):
    #         print(dp[i][j], end=" ")
    #     print("")

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    st = ""
    i = len(s1)
    j = len(s2)

    while i > 0 and j > 0:

        if s1[i-1] == s2[j-1]:
            st += s1[i-1]
            i -= 1
            j -= 1

        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    print(st[::-1])

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            print(dp[i][j], end=" ")
        print("")
    return dp[len(s1)][len(s2)]

# print(lcs("GeeksforGeeks", "GeeksQuiz"))
# print(lcs("abcdxyz", "xyzabcd"))
print(lcs("zxabcdezy", "yzabcdezx"))
