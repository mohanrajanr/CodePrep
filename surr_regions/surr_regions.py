import collections

file = open('test_file.txt')

board = [list(line.strip().split(' ')) for line in file.readlines()]
visited = collections.defaultdict(lambda: False)


def dfs(row, col):
    if not (0 <= row < len(board) and 0 <= col < len(board[row])):
        return
    print("R{} C{} B:{}".format(row, col, board[row][col]))

    if board[row][col] in ['X', '*']:
        return

    board[row][col] = '*'

    dfs(row + 1, col)
    dfs(row, col + 1)
    dfs(row - 1, col)
    dfs(row, col - 1)
    return

for r in range(len(board)):
    for c in range(len(board[r])):
        print(board[r][c], end=" ")
    print(" ")
print("After")
# Border Search
# Col Wise
# First and Last Elements of a row
for index in range(len(board)):
    elements = [0, len(board[index]) - 1]

    for elem in elements:
        print(index, elem)
        if board[index][elem] == 'O':
            dfs(index, elem)

# Row Wise
elements = [0, len(board) - 1]
for elem in elements:
    for index in range(len(board[elem])):
        print(elem, index)
        if board[elem][index] == 'O':
            dfs(elem, index)

for r in range(len(board)):
    for c in range(len(board[r])):
        print(board[r][c], end=" ")
    print(" ")

print("AA")

for r in range(len(board)):
    for c in range(len(board[r])):
        if board[r][c] == '*':
            board[r][c] = 'O'
        else:
            board[r][c] = 'X'

for r in range(len(board)):
    for c in range(len(board[r])):
        print(board[r][c], end=" ")
    print(" ")
