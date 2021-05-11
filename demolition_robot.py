min_val = float('inf')


def demolitionRobot(matrix: list) -> int:
    global min_val
    visited = set()

    def dfs(x, y, curr):

        if 0 <= x < len(matrix) and 0 <= y < len(matrix[x]):
            if (x, y) in visited:
                return

            visited.add((x, y))

            if matrix[x][y] == 9:
                global min_val
                min_val = min(min_val, curr)
                return

            if matrix[x][y] == 1:
                dfs(x + 1, y, curr + 1)
                dfs(x, y + 1, curr + 1)
                dfs(x - 1, y, curr + 1)
                dfs(x, y - 1, curr + 1)

            visited.remove((x, y))

    dfs(0, 0, 0)
    return min_val

min_val = float('inf')
print(demolitionRobot([[1,0,0],[1,0,0],[1,9,1]]))
min_val = float('inf')
print(demolitionRobot([[1,1,1,1],[0,1,1,1],[0,1,0,1],[1,1,9,1],[0,0,1,1]]))
