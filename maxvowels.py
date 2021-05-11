

def maxVowels(s: str, k: int) -> int:

    maxval = 0
    currval = 0
    vows = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(s)):
        if i >= k:
            if s[i - k] in vows and currval > 0:
                currval -= 1

        if s[i] in vows:
            currval += 1

        maxval = max(maxval, currval)
        # print(s[i], currval, maxval)

    return maxval


print(maxVowels("abciiidef", 3))
print(maxVowels("aeiou", 2))
print(maxVowels("leetcode", 3))
print(maxVowels("rhythms", 4))
print(maxVowels("tryhard", 4))
