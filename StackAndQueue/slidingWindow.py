"""
滑动窗口问题,给定一个数组,和一个窗口大小,窗口每走一步,返回此窗口中的最大值
"""


def maxSlidingWindow1(nums, k):
    """
    :param nums:
    :param k:
    :return:
    """
    if not nums:
        return []
    window, res = [], []
    for i, x in enumerate(nums):
        if i >= k and window[0] <= i-k:     # 当窗口完全进入，并且窗口大小超过规定范围时，删除窗口最前面的一个元素
            window.pop(0)
        while window and nums[window[-1]] <= x:     # x为每次新进入窗口的元素，当窗口存在并且刚进来的元素大于窗口最后元素的时候，删除窗口中最后
            window.pop()

        window.append(i)
        if i >= k - 1:
            res.append(nums[window[0]])
    return res


if __name__ == "__main__":
    nums = [5, 8, 4, 6, 3, 6, 1, 0]
    print(maxSlidingWindow1(nums, 3))