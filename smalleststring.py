

def getSmallestString(n: int, k: int) -> str:
    result = ["a" for i in range(n)]
    k -= n

    for i in range(n-1, -1, -1):
        if k <= 0:
            break

        result[i] = chr(97 + min(25, k))
        k -= min(25, k)

    return "".join(result)

print(getSmallestString(3, 27))
print(getSmallestString(5, 73))