from typing import List
import heapq


def kthLargestValue(matrix: List[List[int]], k: int) -> int:

    prev = [matrix[0][0]]
    for i in range(1, len(matrix)):
        prev.append(matrix[0][i] ^ prev[-1])

    a = prev.copy()
    heapq.heapify(a)

    for i in range(1, len(matrix)):
        value = []
        prev_elem = 0
        for j in range(len(matrix[i])):

            elem = matrix[i][j] ^ prev[j]

            if prev_elem:
                elem = elem ^ prev_elem

            value.append(elem)
            prev_elem = elem

            # print(elem)

            heapq.heappush(a, elem)

            while len(a) > k:
                # print(a)
                # print(-heapq.heappop(a))
                heapq.heappop(a)

        # print(value, prev)
        prev = value

    return a[0]

print(kthLargestValue([[5,2],[1,6]], 1))
print(kthLargestValue([[5,2],[1,6]], 2))
print(kthLargestValue([[5,2],[1,6]], 3))
print(kthLargestValue([[5,2],[1,6]], 4))