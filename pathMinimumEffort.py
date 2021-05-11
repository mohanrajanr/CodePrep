from collections import deque
from typing import List


def minimumEffortPath(heights: List[List[int]]) -> int:

    visited = {(0, 0)}

    options = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(0, 0, float('-inf'))])
    max_val = float('-inf')

    while len(queue):

        curr = queue.popleft()
        print(curr)

        if curr[0] == len(heights) - 1 and curr[1] == len(heights[curr[0]]) - 1:
            max_val = max(max_val, curr[2])
            print("M", max_val)
            continue

        for dx, dy in options:
            x = curr[0] + dx
            y = curr[1] + dy

            if 0 <= x < len(heights) and 0 <= y < len(heights[x]) and (x, y) not in visited:
                visited.add((x, y))
                queue.append((x, y, max(curr[2], abs(heights[x][y] - heights[curr[0]][curr[1]]))))

    return max_val

print(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
print(minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
