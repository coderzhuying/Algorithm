"""
给定一个数组,和一个target,判断数组中是否有两个数相加等于target
"""


def twoSum(array, target):
    """
    遍历array，判断target-array[i]是否在set里
    :param array:
    :param target:
    :return:
    """
    length = len(array)
    s = set(array)
    for i in range(length):
        value = target - array[i]
        s.remove(array[i])
        if value in s:
            return i, array.index(value)

    return False


if __name__ == "__main__":
    array = [2, 7, 11, 15]
    target = 9
    print(twoSum(array, target))

