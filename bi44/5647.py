from operator import ixor
from typing import List
from itertools import accumulate


def decode(encoded: List[int]) -> List[int]:

    n = len(encoded) + 1

    first = 1
    for i in range(2, n + 1):
        first ^= i

    for i in range(1, len(encoded), 2):
        first ^= encoded[i]
        # print(encoded[i], first)

    # print(first)
    output = list(accumulate([first] + encoded, ixor))

    return output

print(decode([3, 1]))
print(decode([6,5,4,6]))
