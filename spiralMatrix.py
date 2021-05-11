from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:

    # (0, 0)
    # (0, 1) y + 1
    # (0, 2) y + 1
    #
    # (1, 2) x + 1
    # (2, 2) x + 1
    #
    # (2, 1) y - 1
    # (2, 0) y - 1
    #
    # (1, 0) x - 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    matrix_size = [len(matrix), len(matrix[0])]

    for i in range(0, max(matrix_size), 2):
        # print("start:{}".format(i))
        x, y = i, i
        ms = matrix_size[0]
        for dx, dy in directions:
            for k in range(ms - i - 1):
                print(x, y)

                x += dx
                y += dy
            ms = matrix_size[0] if ms == matrix_size[1] else matrix_size[1]


# print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
