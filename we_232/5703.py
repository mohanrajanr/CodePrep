from typing import List
import heapq


def maxAverageRatio(classes: List[List[int]], extraStudents: int) -> float:

    a = []
    heapq.heapify(a)
    for c in classes:
        heapq.heappush(a, ('{:.5f}'.format(c[0]/c[1]), c[0], c[1]))

    # print("Before:{}".format(a))
    while extraStudents:
        least = heapq.heappop(a)
        p = least[1] + 1
        t = least[2] + 1
        print(least, p/t, p, t)
        heapq.heappush(a, ('{:.5f}'.format(p/t), p, t))
        extraStudents -= 1

    s = 0
    for i in a:
        s += float(i[0])

    return '{:.5f}'.format(s/len(a))

# print(maxAverageRatio([[1,2],[3,5],[2,2]], 2))
print(maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))
