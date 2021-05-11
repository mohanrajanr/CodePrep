from typing import List


def minimumHammingDistance(source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

    # Sort Swaps properly
    for swap in allowedSwaps:
        if swap[0] > swap[1]:
            swap[0], swap[1] = swap[1], swap[0]

    allowedSwaps.sort(key=lambda x: x[0])

    print(allowedSwaps)

    distance = 0
    for i in range(len(target)):

        if source[i] == target[i]:
            continue

        for swap in allowedSwaps:

            if swap[0] > i:
                break

            if swap[0] == i:
                if source[swap[1]] == target[i]:
                    source[swap[0]], source[swap[1]] = source[swap[1]], source[swap[0]]
                    break

        if source[i] != target[i]:
            distance += 1

    return distance


print(minimumHammingDistance([1,2,3,4], [2,1,4,5], [[0,1],[2,3]]))
print(minimumHammingDistance([1,2,3,4], [1,3,2,4], []))
print(minimumHammingDistance([5,1,2,4,3], [1,5,4,2,3], [[0,4],[4,2],[1,3],[1,4]]))
