from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    ans = 0
    stack = [-1]
    heights.append(0)
    for ind in range(len(heights)):

        while heights[stack[-1]] > heights[ind]:
            h = heights[stack.pop()]
            w = ind - stack[-1] - 1
            ans = max(ans, w*h)
        stack.append(ind)
    heights.pop()
    return ans

print(largestRectangleArea([2,1,5,6,2,3]))
print(largestRectangleArea([1, 2, 2]))
print(largestRectangleArea([1,2,3,4,5]))
# assert largestRectangleArea([2,1,5,6,2,3]) == 10
