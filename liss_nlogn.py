from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    dp = [[nums[0]]]

    for i in range(1, len(nums)):
        to_append = False
        for j in range(len(dp)):
            if dp[j][-1] < nums[i]:
                to_append = j
            elif dp[j][-1] == i:
                continue

        if to_append != False:
            dp[to_append].append(nums[i])
        else:
            dp.append([nums[i]])

    print(dp)
    return max([len(d) for d in dp])

print(lengthOfLIS([10,9,2,5,3,7,101,18]), 4)
# print(lengthOfLIS([0,1,0,3,2,3]), 4)
# print(lengthOfLIS([7,7,7,7,7,7,7]), 1)
# print(lengthOfLIS([1,3,6,7,9,4,10,5,6]), 6)
