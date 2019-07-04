def candy(candies, nums):
    b = 0
    i = 1
    res = [0 for _ in range(nums)]
    while candies != 0:
        if i == nums:
            b += 1
        candy = i
        if candy < candies:
            res[(i-1) % nums] += candy
            candies -= candy
        else:
            res[(i-1) % nums] += candies
            candies = 0
        i += 1
    return res


candies = 7
nums = 4
print(candy(candies, nums))