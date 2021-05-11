from typing import List


def findPeakElement(nums: List[int]) -> int:

    l = 0
    r = len(nums) -1

    while l < r:
        mid = l + (r - l)//2

        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid

    return l


print(findPeakElement([1,2,3,1]))
print(findPeakElement([1,2,1,3,5,6,4]))
