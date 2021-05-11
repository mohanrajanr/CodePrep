from typing import List

# TODO: NOT WORKING FOR LONG VALUES. Change it.
def longestSubarray(nums: List[int], limit: int) -> int:
    longest = 1
    start = 0

    for i in range(1, len(nums)):

        # while start < i and abs(nums[i] - nums[start]) > limit:
        #     # print("changing start", start, i)
        #     start += 1

        for j in range(i, start-1, -1):
            if abs(nums[i] - nums[j]) <= limit:
                # print(nums[i], nums[j])
                longest = max(longest, i - j + 1)
            else:
                # print("start = j", j)
                start = j + 1
                break

    return longest


print(longestSubarray([8,2,4,7], 4))
print(longestSubarray([10,1,2,4,7,2], 5))
print(longestSubarray([4,2,2,2,4,4,2,2], 0))
print(longestSubarray([1,5,6,7,8,10,6,5,6], 4))
