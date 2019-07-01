"""
打家劫舍问题，不能选相邻的元素，可以选多个元素，使和最大
思路：选与不选问题.
    如果要选第i个元素,则不能选i-1,所以得到的结果是array[i]+opt[i-2]
    如果不选第i个,得到的结果应该是opt[i-1]
    在二者之中取较大即可
"""


def rec_opt(array, i):
    """
    递归解决:类似于斐波拉切问题,不处理重叠子问题,倒着计算.
    :param array:
    :param i:
    :return:
    """
    if i == 0:
        return array[0]
    elif i == 1:
        return max(array[0], array[1])
    else:
        return max(rec_opt(array, i-2)+array[i], rec_opt(array, i-1))


def dp_opt(array):
    """
    非递归:正着计算,这样避免重叠子问题
    :param array:
    :return:
    """
    opt = []
    opt.append(array[0])
    opt.append(max(array[0], array[1]))
    length = len(array)
    for i in range(2, length):
        opt.append(max(opt[i-2]+array[i], opt[i-1]))

    return opt


if __name__ == "__main__":
    # [4, 1, 1, 9, 1]
    print(dp_opt([1, 2, 4, 1, 7, 8, 3]))
    print(rec_opt([4, 1, 1, 9, 1], 4))