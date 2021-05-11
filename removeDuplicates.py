from typing import List


def removeDuplicates(nums: List[int]) -> int:
    i, j = 1, 1
    count = 1
    curr = nums[0]
    while j < len(nums):
        # print(nums[i], nums[j], i, j, curr, count)
        if nums[j] == curr:

            if count < 2:
                count += 1
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        else:
            count = 1
            curr = nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    return i

# nums = [1,1,1,2,2,3]
# print(removeDuplicates(nums))
# print(nums)
#
# nums = [0,0,1,1,1,1,2,3,3]
# print(removeDuplicates(nums))
# print(nums)
