from typing import List


def decode(encoded: List[int], first: int) -> List[int]:
    output = [0 for i in range(len(encoded)+1)]
    output[0] = first

    for i in range(1, len(output)):
        output[i] = encoded[i-1] ^ output[i-1]

    # print(output)
    return output

print(decode([1,2,3], 1))
print(decode([6,2,7,3], 4))
