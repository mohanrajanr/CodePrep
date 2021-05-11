def calculateMinimumHP(dungeon):
    m = len(dungeon)
    n = len(dungeon[0])

    for i in range(m):
        for j in range(n):
            dungeon[i][j] = -dungeon[i][j]

    for i in range(1, m):
        if dungeon[i-1][0] + dungeon[i][0] < 0:
            dungeon[i][0] = float('inf')
        else:
            dungeon[i][0] += dungeon[i-1][0]

    for i in range(1, n):
        if dungeon[0][i-1] + dungeon[0][i] < 0:
            dungeon[0][i] = float('inf')
        else:
            dungeon[0][i] += dungeon[0][i-1]

    for i in range(1, m):
        for j in range(1, n):
            minval = min(dungeon[i-1][j], dungeon[i][j-1])
            if dungeon[i][j] + minval < 0:
                dungeon[i][j] = float('inf')
            else:
                dungeon[i][j] += minval

    return dungeon[-1][-1] + 1

print(calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
