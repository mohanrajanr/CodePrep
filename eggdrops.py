
eggs = 4
floors = 5000

dp = [[0 for i in range(eggs+1)] for j in range(floors+1)]

# # For Floor 1 its always 1
# for index, egg_n_floor in enumerate(dp):
#     if index == 0:
#         continue
#     egg_n_floor[1] = index
#
# # For Egg 1 It will be equal to floor value
# dp[1] = [1 for i in range(eggs + 1)]
# dp[1][0] = 0


def print_board():
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            print(dp[i][j], end=" ")
        print("")


def solve():

    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1

        if dp[i][j] >= floors:
            print(i)
            return

# print("Base")
# print_board()
solve()
print("Solved")
print_board()


# K = eggs
# N = floors
# dp = [[0] * (K + 1) for _ in range(N + 1)]
#
# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         dp[i][j] = 1 + dp[i - 1][j - 1] + dp[i - 1][j]
#     if dp[i][j] >= N:
# #         print("RES", i)
#
# print_board()