from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    dp = [1 for i in range(len(nums))]

    for i in range(1, len(nums)):
        res = 0
        for j in range(i):
            if nums[j] < nums[i]:
                res = dp[j] + 1
                dp[i] = max(dp[i], res)

    print(dp)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
