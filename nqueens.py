
n = row = col = 5

board = [[0 for i in range(n)] for j in range(n)]


def print_board():
    for i in range(row):
        for j in range(col):
            print(board[i][j], end=" ")
        print("")

print_board()


def is_safe(r, c):

    # Row
    for i in range(c):
        if board[r][i] == 1:
            return False

    # Diagonals - Left Top
    for i, j in zip(range(r-1, -1, -1), range(c-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Diagonals - Left bottom
    for i, j in zip(range(r+1, row), range(c - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def n_queens(c=0):
    if c >= col:
        return True

    for r in range(row):

        if is_safe(r, c):

            board[r][c] = 1

            if n_queens(c+1):
                return True

            board[r][c] = 0

if n_queens():
    print_board()
else:
    print("Nope")