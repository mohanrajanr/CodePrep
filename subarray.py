def subarraySum(nums, k):
    count = dict()
    curr = 0
    res = 0

    count[0] = 1
    for i in nums:
        curr += i
        res += count.get(curr - k, 0)
        count[curr] = count.get(curr, 0) + 1

    return res


print(subarraySum([1, 1, 1], 2))
print(subarraySum([1, 2, 3], 3))
