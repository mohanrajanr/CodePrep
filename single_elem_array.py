def singleNonDuplicate(nums) -> int:
    def condition(k):
        div = k % 2 == 0
        if div:
            if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                return True
        else:
            if k > 0 and nums[k] == nums[k - 1]:
                return True
        return False

    l = 0
    r = len(nums) - 1

    while l < r:
        m = l + (r - l) // 2
        print(l, r, m, nums[m])

        if condition(m):
            # print("Yes")
            l = m + 1
        else:
            # print("No")
            r = m

    return nums[l]


print("Test 1:{}".format(singleNonDuplicate([1,1,2,3,3,4,4,8,8])))
print("Test 2:{}".format(singleNonDuplicate([3,3,7,7,10,11,11])))
print("Test 3:{}".format(singleNonDuplicate([3,7,7,10,10,11,11])))
print("Test 4:{}".format(singleNonDuplicate([3,3,7,7,10,10,11])))