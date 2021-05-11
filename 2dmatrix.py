from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:

    rows = len(matrix)
    cols = len(matrix[0])

    l = 0
    r = (rows * cols) - 1

    while l < r:
        mid = l + (r - l)//2

        row = mid // cols
        col = mid % cols

        # print(row, col, mid, matrix[row][col])
        if matrix[row][col] < target:
            l = mid + 1
        else:
            r = mid
    # print(l, matrix[l//cols][l%cols])
    return matrix[l // cols][l % cols] == target

# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))


def searchMatrix2(matrix: List[List[int]], target: int) -> bool:

    rows = len(matrix)
    cols = len(matrix[0])

    i = 0
    j = cols - 1

    while 0 <= i < rows and 0 <= j < cols:

        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1

    return False


print(searchMatrix2([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
print(searchMatrix2([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
