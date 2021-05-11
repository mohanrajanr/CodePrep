from typing import List


# def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
#     result = []
#
#     def backtracking(pos, curr_sum, curr_list):
#         if curr_sum == target:
#             result.append(curr_list[:])
#             return
#         if curr_sum > target:
#             return
#         if pos >= len(candidates):
#             return
#
#         curr_list.append(candidates[pos])
#         backtracking(pos, curr_sum+candidates[pos], curr_list)
#         curr_list.pop()
#
#         backtracking(pos+1, curr_sum, curr_list)
#
#         return
#
#     backtracking(0, 0, [])
#     return result
#
#
# print(combinationSum([2,3,6,7], 7))
# print(combinationSum([2,3,5], 8))
# print(combinationSum([2], 1))


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = set()

    def backtracking(pos, curr_sum, curr_list):
        if curr_sum == target:
            result.add(tuple(curr_list))
            return
        if curr_sum > target:
            return
        if pos >= len(candidates):
            return

        curr_list.append(candidates[pos])
        backtracking(pos+1, curr_sum+candidates[pos], curr_list)
        curr_list.pop()

        backtracking(pos+1, curr_sum, curr_list)

        return

    candidates.sort()
    backtracking(0, 0, [])
    return [list(val) for val in result]


print(combinationSum([10,1,2,7,6,1,5], 8))
print(combinationSum([2,5,2,1,2], 5))
