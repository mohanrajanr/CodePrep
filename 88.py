def merge(nums1: list, m: int, nums2: list, n: int):
    index = len(nums1) - 1
    n1_i = m - 1
    n2_i = n - 1

    while index >= 0:

        n1 = n2 = float('-inf')

        if n1_i >= 0:
            n1 = nums1[n1_i]
        if n2_i >= 0:
            n2 = nums2[n2_i]

        if n1 > n2:
            nums1[index] = n1
            n1_i -= 1
        else:
            nums1[index] = n2
            n2_i -= 1

        index -= 1

    return nums1


# Test Case
test_cases = [dict(input=dict(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3),output=[1,2,2,3,5,6]),
              dict(input=dict(nums1=[4,5,6,0,0,0], m=3, nums2=[1,2,3], n=3),output=[1,2,3,4,5,6]),
              dict(input=dict(nums1=[1], m=1, nums2=[], n=0),output=[1])]

for index, data in enumerate(test_cases, 1):
    act_output = merge(**data['input'])
    print("Test Case:{} Validity:{}".format(index, act_output == data['output']))
    print("Input:{} Expected:{} Act:{}".format(data['input'], data['output'], act_output))
