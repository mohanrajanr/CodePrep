from typing import List


def canPartition(nums: List[int]) -> bool:
    if len(nums) < 2:
        return False

    totalSum = sum(nums)
    if totalSum & 1 == 1:
        return False
    totalSum >>= 1

    dp = [[False for _ in range(totalSum + 1)] for _ in range(len(nums) + 1)]
    dp[0][0] = True

    # for i in range(len(nums) + 1):
    #     for j in range(totalSum + 1):
    #         print(dp[i][j], end=" ")
    #     print("")

    for i in range(1, len(nums) + 1):
        dp[i][0] = True

    for i in range(1, totalSum + 1):
        dp[0][i] = False

    for i in range(1, len(nums) + 1):
        for j in range(1, totalSum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i-1]:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i][j]

    return dp[len(nums)][totalSum]

print(canPartition([1,5,11,5]))
print(canPartition([1, 2, 5]))
print(canPartition([2, 3, 1]))
print(canPartition([1,2,3,5]))
print(canPartition([83,22,11,15,50,78,16,38,23,77,81,16,3,72,94,53,91,73,7,74,86,12,36,51,5,80,47,68,29,71,5,16,26,4,16,26,6,8,48,93,27,10,93,61,34,50,50,82,59,10,7,94,18,5,5,97,21,9,71,72,29,87,83,31,71,61,79,49,27,18,72,55,75,1,67,54,90,87,93,49,66,8,11,85,74,50,45,33,33,85,35,86,57,26,29,64,75,73,5,71]))
print(canPartition([38,7,20,83,13,44,87,70,45,54,23,72,81,62,33,55,16,96,9,64,15,88,45,97,43,55,56,43,13,29,79,27,26,50,25,5,24,61,48,32,52,62,25,77,18,4,59,73,70,92,2,36,94,4,24,71,42,11,41,94,20,82,14,71,45,80,35,61,31,61,46,47,40,80,52,90,52,6,75,28,67,68,8,77,19,2,85,69,35,14,58,67,45,66,87,6,24,88,11,24]))
