
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
visited = set()


def dfs(row, col):
    if not (0 <= row < len(grid) and 0 <= col < len(grid[row])):
        return

    if (row, col) in visited:
        return

    if grid[row][col] != '1':
        return

    visited.add((row, col))

    dfs(row + 1, col)
    dfs(row - 1, col)
    dfs(row, col + 1)
    dfs(row, col - 1)
    return


total_islands = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if (r, c) not in visited and grid[r][c] == '1':
            total_islands += 1
            dfs(r, c)

print(total_islands)