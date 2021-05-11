from typing import List
import heapq


def minimumTimeRequired(jobs: List[int], k: int) -> int:

    worker = [0 for i in range(k)]

    heapq.heapify(jobs)
    while len(jobs):

        job_peek = jobs[0]
        work_peek = worker[0]

        popped = heapq.heappop(worker)
        elem = popped + heapq.heappop(jobs)
        print(worker, elem)
        heapq.heappush(worker, elem)

    print(worker)
    return max(worker)

print(minimumTimeRequired([3,2,3], 3))
print(minimumTimeRequired([1,2,4,7,8], 2))