import collections
from typing import List


def restoreArray(adjacentPairs: List[List[int]]) -> List[int]:

    graph = collections.defaultdict(list)
    for ap in adjacentPairs:
        graph[ap[0]].append(ap[1])
        graph[ap[1]].append(ap[0])

    start_elem = [key for key, value in graph.items() if len(value) == 1][0]
    queue = [start_elem]
    processed = {start_elem}

    for i in range(len(adjacentPairs)):
        elems = graph[queue[-1]]

        if len(elems) == 1:
            other_elem = elems[0]
        else:
            other_elem = elems[0] if elems[0] not in processed else elems[1]

        queue.append(other_elem)
        processed.add(other_elem)

        # print(queue[-1], elems, processed)

    return queue


print(restoreArray([[2,1],[3,4],[3,2]]))
print(restoreArray([[4,-2],[1,4],[-3,1]]))
print(restoreArray([[100000,-100000]]))

