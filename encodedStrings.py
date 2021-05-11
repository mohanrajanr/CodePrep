from collections import defaultdict


def encodedString(value: int) -> (int, list):

    dp = defaultdict(list)

    def run_dp(val):
        # print("trying:{}".format(val))
        if not val:
            return []

        if val in dp:
            # print("Cache:{}".format(dp[val]))
            return dp[val]

        res = []

        unit = val % 10
        others = val // 10

        unit_rest_list = run_dp(others)
        if unit > 0:
            if unit_rest_list:
                for rest in unit_rest_list:
                    res.append('{}{}'.format(rest, chr(96 + unit)))
            else:
                res.append(chr(96 + unit))

        if others > 0:
            ten = others % 10
            ten_others = others // 10

            if ten < 3 and unit < 7:

                ten_rest_list = run_dp(ten_others)
                ten_char_int = 10 * ten + unit
                if ten_rest_list:
                    for rest in ten_rest_list:
                        res.append('{}{}'.format(rest, chr(96 + ten_char_int)))
                else:
                    res.append(chr(96 + ten_char_int))

        # print("Stored:{} {}".format(val, res))
        dp[val] = res
        return dp[val]

    result = run_dp(value)
    return len(result), result


# print(encodedString(11))
# print(encodedString(2))
# print(encodedString(23))
# print(encodedString(26))
# print(encodedString(27))
# print(encodedString(20))
print(encodedString(1123))
print(encodedString(1127694948442032702488512345))
