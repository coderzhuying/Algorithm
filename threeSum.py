"""
给定一个数组，找出数组里三个数和为0的所有三元组
"""


def threeSum(nums):
    """
    使用twosum的方法化为两重循环
    :param nums:
    :return:
    """
    if len(nums) < 3:
        return []
    nums.sort()     # 提高效率
    res = set()
    for i, v in enumerate(nums[:-2]):
        if i >= 1 and v == nums[i-1]:   # 如果当前v和前面的一样，则不需用再次进行循环判断
            continue
        d = {}                          # 用来判断-(v+x)是否存在的字典
        for x in nums[i+1:]:
            if x not in d:              # 如果x不在字典中，将-(v+x)放入字典，这样下次遍历到-(v+x)时，就可以判断是否在字典中,
                d[-v-x] = 1
            else:
                res.add((v, -v-x, x))

    return list(res)


def threeSum2(nums):
    """
    排序之后，遍历每个元素时，从两边向中间逼近
    :param nums:
    :return:
    """
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:       # 判重处理
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1

    return res


if __name__ == "__main__":
    array = [1,0,-1,6,3,-3]
    print(threeSum2(array))