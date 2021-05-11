from typing import List


def canChoose(groups: List[List[int]], nums: List[int]) -> bool:

    index = len(nums) - 1
    hasMatched = False
    while groups and nums:
        tu = tuple(groups.pop())

        # print("Checking :{}".format(tu))
        hasMatched = False

        while index - len(tu) + 1 >= 0:
            values = nums[index - len(tu) + 1: index+1]

            # print(values)
            if tuple(values) == tu:
                hasMatched = True
                # print("MM")

                t = len(tu)
                while t:
                    index -= 1
                    nums.pop()
                    t -= 1

                break

            index -= 1
            nums.pop()

    # print(groups)
    # print(nums)
    return hasMatched and len(groups) == 0

print(canChoose([[1,-1,-1],[3,-2,0]], [1,-1,0,1,-1,-1,3,-2,0]))
print(canChoose([[10,-2],[1,2,3,4]], [1,2,3,4,10,-2]))
print(canChoose([[1,2,3],[3,4]], [1,-1,0,1,-1,-1,3,-2,0]))
print(canChoose([[1,2,3],[3,4]], [7,7,1,2,3,4,7,7]))