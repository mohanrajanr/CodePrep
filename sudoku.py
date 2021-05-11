
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
row = col = len(board)


def print_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print("")


def is_safe(r, c, val):

    rloc = r
    cloc = c
    rloc -= r % 3
    cloc -= c % 3

    rowSafe = all(board[r][_] != val for _ in range(col))
    colSafe = all(board[_][c] != val for _ in range(row))
    squareSafe = all(board[a][b] != val for a in range(rloc, rloc+3) for b in range(cloc, cloc+3))
    return rowSafe and colSafe and squareSafe


def get_next_one():
    for i in range(row):
        for j in range(col):
            if board[i][j] == '.':
                return i, j
    return -1, -1


def solve():

    r, c = get_next_one()
    if (r, c) == (-1, -1):
        return True

    for i in range(1, 10):

        if is_safe(r, c, str(i)):
            board[r][c] = str(i)

            if solve():
                return True

            board[r][c] = '.'

    return False


print("UnSolved:")
print_board()

if solve():
    print("Solved")
    print_board()
else:
    print("Cannot Solve")