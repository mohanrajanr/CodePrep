from typing import List


def closestCost(baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
    closest = [float('-inf'), float('inf')]

    def add_to(value):
        if value <= target:
            closest[0] = max(closest[0], value)
        else:
            closest[1] = min(closest[1], value)

    def backtrack(cost, index):

        # print(cost, toppingCosts[index] + cost, (toppingCosts[index] * 2) + cost)
        add_to(cost)

        if index >= len(toppingCosts):
            return

        backtrack(toppingCosts[index] + cost, index + 1)
        backtrack((toppingCosts[index] * 2) + cost, index + 1)
        backtrack(cost, index + 1)

    for cost in baseCosts:
        backtrack(cost, 0)

    # print(closest)
    return int(closest[0]) if abs(target - closest[0]) <= abs(closest[1] - target) else int(closest[1])

print(closestCost([1, 7], [3, 4], 10))
print(closestCost([2, 3], [4, 5, 100], 18))
print(closestCost([3, 10], [2, 5], 9))
print(closestCost([10], [1], 1))
