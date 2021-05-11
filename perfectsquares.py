import math


def numSquares(n: int) -> int:
    res = 0
    while n:
        print(n, pow(math.floor(math.sqrt(n)), 2))
        n = n - pow(math.floor(math.sqrt(n)), 2)
        res += 1

    return res


print(numSquares(12))