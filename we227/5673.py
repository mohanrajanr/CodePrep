def maximumScore(a: int, b: int, c: int) -> int:
    turns = 0

    while not (((a == 0) and (b == 0)) or ((b == 0) and (c == 0)) or ((a == 0) and (c == 0))):
        print(a, b, c, turns)
        if a % b == 0:
            a -= b
            b = 0
            turns += a

        elif a % b == 0:
            b -= a
            a = 0
            turns += b

        elif b % c == 0:
            b -= c
            b = 0
            turns += b

        elif c % b == 0:
            c -= b
            c = 0
            turns += c

        elif c % a == 0:
            c -= a
            a = 0
            turns += c

        elif a % c == 0:
            a -= c
            c = 0
            turns += a

    return turns


print(maximumScore(2, 4, 6))
print(maximumScore(4, 4, 6))
print(maximumScore(1, 8, 8))