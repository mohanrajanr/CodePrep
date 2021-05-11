from typing import List


def highestPeak(isWater: List[List[int]]) -> List[List[int]]:

    heighestPeak = [[0 for i in range(len(isWater[j]))] for j in range(len(isWater))]

    for i in range(len(isWater)):
        for j in range(len(isWater)):
            if i == 0 or j == 0:
                heighestPeak[i][j] = 0 if isWater[i][j] else 1
            else:
                heighestPeak[i][j] = min(heighestPeak[i-1][j], heighestPeak[i][j-1]) + 1

    return heighestPeak

print(highestPeak([[0, 1],[0, 0]]))
print(highestPeak([[0,0,1],[1,0,0],[0,0,0]]))