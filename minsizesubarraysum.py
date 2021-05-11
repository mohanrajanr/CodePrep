from typing import List


def minSubArrayLen(s: int, nums: List[int]) -> int:
    if not len(nums) or sum(nums) < s:
        return 0

    st = 0
    p = 0
    curr_sum = 0
    output = 0

    while p < len(nums):
        print(curr_sum, st, p, output)
        if curr_sum > s:
            curr_sum -= nums[st]
            st += 1
        else:
            output = (p - st + 1)
            curr_sum += nums[p]
            p += 1

    return output

print(minSubArrayLen(7, [2,3,1,2,4,3]))
