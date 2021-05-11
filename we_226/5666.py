def checkPartitioning(s: str) -> bool:

    dp = dict()

    def isPalin(st):
        if st in dp:
            return dp[st]

        last = -1
        for first in st:
            if first != st[last]:
                dp[st] = False
                return dp[st]
            last = last - 1

        dp[st] = True
        return dp[st]

    for i in range(1, len(s) - 1):
        for j in range(i+1, len(s)):
            # print(s[0:i], s[i:j], s[j:])
            if isPalin(s[0:i]) and isPalin(s[i:j]) and isPalin(s[j:]):
                return True

    return False

print(checkPartitioning("abcbdd"))
print(checkPartitioning("bcbddxy"))
