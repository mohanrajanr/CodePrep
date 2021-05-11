from typing import List


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print(" ")


def pacificAtlantic(matrix: List[List[int]]) -> List[List[int]]:

    def boundary(i, j):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]):
            return True
        return False

    p_d = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    a_d = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

    # Process PD
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            for diff_i, diff_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                if boundary(i+diff_i, j+diff_j) or (p_d[i+diff_i][j+diff_j] and matrix[i+diff_i][j+diff_j] <= matrix[i][j]):
                    p_d[i][j] = 1
                    break

    # print("PD")
    # print_matrix(p_d)

    # Process AD
    for i in range(len(matrix)-2, 0, -1):
        for j in range(len(matrix[i])-2, 0, -1):
            for diff_i, diff_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                if boundary(i+diff_i, j+diff_j) or (a_d[i+diff_i][j+diff_j] and matrix[i+diff_i][j+diff_j] <= matrix[i][j]):
                    a_d[i][j] = 1
                    break

    # print("AD")
    # print_matrix(a_d)

    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if p_d[i][j] and a_d[i][j]:
                res.append([i, j])

    return res


print("1")
out = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
test_out = set([tuple(l) for l in out])
for l in pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]):
    if tuple(l) not in test_out:
        print("No:", l)
        continue
    print("Yes:", l)

print("2")
out = [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
test_out = set([tuple(l) for l in out])
for l in pacificAtlantic([[1,2,3],[8,9,4],[7,6,5]]):
    if tuple(l) not in test_out:
        print("No:", l)
        continue
    print("Yes:", l)

print("Done")