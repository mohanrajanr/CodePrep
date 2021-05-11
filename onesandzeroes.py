from typing import List


def findMaxForm(strs: List[str], m: int, n: int) -> int:
    dp = dict()

    def do_dp(index, m, n):
        if m < 0 or n < 0:
            return float('-inf')

        if index >= len(strs):
            return 0

        if m == 0 and n == 0:
            return 0

        if (index, m, n) in dp:
            # print("cache")
            return dp[(index, m, n)]

        dp[(index, m, n)] = max(do_dp(index+1, m-strs[index].count("0"), n-strs[index].count("1")) + 1, do_dp(index+1, m, n))

        # print('normal')
        return dp[(index, m, n)]

    return do_dp(0, m, n)


print(findMaxForm(["10","0001","111001","1","0"], 5, 3))
print(findMaxForm(["10","0", "1"], 1, 1))
print(findMaxForm(["00","000"], 1, 10))