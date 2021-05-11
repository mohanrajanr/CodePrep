def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print("")


def rotatematrix(matrix: list):

    row_wise = list(zip(*matrix))

    return [r[::-1] for r in row_wise]

    # for i in range(len(matrix)-1, 0, -2):
    #
    #     for j in range(0, len(matrix), 2):
    #
    #         matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]

            # temp = matrix[0][j]
            #
            # options = [(0, i-1), (i-1, i-1), (i-1, 0), (0, 0)]
            # for k in range(4):
            #     dx, dy = options[k]
            #     print((dx + j) % i, (dy + j) % i)
            #     matrix[dx][(dy + j) % i], temp = temp, matrix[dx][(dy + j) % i]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print_matrix(matrix)
rotatematrix(matrix)
print_matrix(matrix)