from typing import List


def findLHS(nums: List[int]) -> int:
    currValue = 0
    longestValue = 0
    minv = maxv = nums[0]

    for i in range(1, len(nums)):

        minv = maxv = nums[i]
        currValue = 0

        for j in range(i-1, -1, -1):
            minv = min(minv, nums[j])
            maxv = max(maxv, nums[j])

            if maxv - minv == 1:
                currValue += i - j

            print(nums[j], nums[i], minv, maxv, currValue)

        longestValue = max(longestValue, currValue)

    return longestValue


print(findLHS([1,3,2,2,5,2,3,7]))
# print(findLHS([1,2,3,4]))
# print(findLHS([1,1,1,1]))
