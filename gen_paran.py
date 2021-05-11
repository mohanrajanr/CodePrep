def generateParenthesis(n: int):
    def dfs(n, op, s):
        # print(n, op, s)
        if n == 0 and op == 0:
            return [s]

        ret = []
        if op:
            ret.extend(dfs(n, op - 1, s + ')'))
        if n:
            ret.extend(dfs(n - 1, op + 1, s + '('))
        return ret

    return dfs(n-1, 1, '(')


print(generateParenthesis(1))
print(generateParenthesis(3))
