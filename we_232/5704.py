
def maxScore(nums, k):

    maxVal = 0
    for i in range(k+1):
        for j in range(k, len(nums)):
            # print(i, j, min(nums[i:j+1]) * (j - i + 1))
            maxVal = max(maxVal, min(nums[i:j+1]) * (j - i + 1))

    return maxVal

print(maxScore([1,4 , 3, 7, 4, 5], 3))
print(maxScore([5,4,4,5,4,1,1,1], 0))