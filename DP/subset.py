"""
判断在一个均为正数的数组里能否拼成给定的k
[1,2,3,6,8,1] k=7 返回True,k=0,返回False
"""
import numpy as np


def rec_subset(array, i, target):
    """
    同样，选与不选的问题,递归来说,需要找到递归出口和递归方程
    :param array:
    :param i:
    :param target:递归到第i个元素时target的值
    :return:
    """
    if target == 0:             # 当递归到target=0时说明已经可以拼成target，返回True
        return True
    elif i == 0:                # 当递归到第一个元素时，如果target=array[0],说明可以拼成，否则不能拼成
        return array[0] == target
    elif array[i] > target:     # 因为全是正数所以当array[i] > target时，就直接走不选当前元素的这条路
        return rec_subset(array, i-1, target)
    else:
        A = rec_subset(array, i-1, target-array[i])     # 选i-1，target减去当前array的值，继续递归
        B = rec_subset(array, i-1, target)              # 不选i-1，target不变继续递归
        return A or B                                   # 这两条路只要走成功一条就可以了


def dp_subset(array, S):
    """
    动态规划做,为了避免求重复子问题,从前往后做,此时要构建一个二位数组
    array = [3, 34, 4, 12, 5, 2], S=9
        0   1   2   3   4   5   6   7   8   9
    0   F   F   F   T   F   F   F   F   F   F
    1   T
    2   T
    3   T
    4   T
    5   T
    :param array:
    :param S:要拼成的关键字
    :return:
    """
    subset = np.zeros((len(array), S+1), dtype=bool)
    subset[:, 0] = True
    subset[0, :] = False
    subset[0, array[0]] = True
    for i in range(1, len(array)):
        for s in range(1, S+1):
            if array[i] > s:
                subset[i, s] = subset[i-1, s]
            else:
                A = subset[i-1, s-array[i]]
                B = subset[i-1, s]
                subset[i, s] = A or B

    r, c = subset.shape

    return subset[r-1, c-1]


if __name__ == "__main__":
    array = [3, 34, 4, 12, 5, 2]
    # print(rec_subset(array, len(array)-1, 13))
    print(dp_subset(array, 10))