def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    def isPalin(st, en):

        while st > 0 and en < len(s) and s[st] == s[en]:
            st -= 1
            en += 1

        if st < 0:
            st = 0
        if en >= len(s):
            en = len(s) - 1

        if s[st] != s[en]:
            st += 1
            en -= 1

        return s[st:en]

    res = s[0]

    for i in range(len(s)):
        res = max(isPalin(i, i), isPalin(i, i+1), res, key=len)
    return res


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("babababd"))
print(longestPalindrome("a"))
print(longestPalindrome("ac"))
print(longestPalindrome("bb"))
