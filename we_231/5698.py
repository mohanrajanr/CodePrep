import time
from typing import List


def minElements(nums: List[int], limit: int, goal: int) -> int:
    currsum = sum(nums)

    reqd = abs(goal - currsum)
    val = 0
    while reqd > 0:
        print(limit, reqd, val)
        time.sleep(1)

        if limit < reqd:
            val += reqd // limit
            reqd = reqd % limit
        else:
            val += 1
            break

    return val


print(minElements([1,-1,1], 3, -4))
print(minElements([1,-10,9,1], 100, 0))
print(minElements([2,5,5,-7,4], 7, 464680098))
print(minElements([-1,0,1,1,1], 1, 771843707))