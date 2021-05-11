def asum(nums: list) -> int:
    # dp = [abs(n) for n in nums]
    # for index, n in enumerate(nums):
    #     for j in range(index, -1, -1):
    #         print(j, index, nums[j:index], abs(sum(nums[j:index])))
    #         dp[index] = max(dp[index], abs(sum(nums[j:index + 1])))

    # return max(dp)

    currso = maxso = float('-inf')
    currnso = minso = float('inf')

    for i in nums:
        currso = max(currso + i, i)
        maxso = max(maxso, currso)

        currnso = min(i, currnso + i)
        minso = min(minso, currnso)

        # print(currnso, currso, minso, maxso)

    return max(abs(minso), maxso)


print(asum([1,-3,2,3,-4]))
print(asum([2,-5,1,-4,3,-2]))
print(asum([-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9]))