from typing import List


def maxSatisfied(customers: List[int], grumpy: List[int], X: int) -> int:

    already_filled = 0
    for i in range(len(customers)):
        if not grumpy[i]:
            already_filled += customers[i]
            customers[i] = 0

    max_window = curr_window = 0
    for i in range(len(customers)):
        curr_window += customers[i]

        if i >= X:
            curr_window -= customers[i-X]

        max_window = max(max_window, curr_window)

    return already_filled + max_window


print(maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))
print(maxSatisfied([3], [1], 1))
print(maxSatisfied([5, 8], [0, 1], 1))
print(maxSatisfied([10, 1, 7], [0, 0, 0], 2))