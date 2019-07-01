"""
二维数组中行递增，列递增，给
出一个数判断数组中是否存在
"""


def find(target, array):
    row = len(array)
    col = len(array[0])
    i = 0
    j = col - 1
    while i < row and j >= 0:
        if target > array[i][j]:
            i = i + 1
        elif target == array[i][j]:
            return i, j
        else:
            j = j - 1
    return -1, -1


if __name__ == '__main__':
    array = [
                [1, 2, 8, 9],
                [2, 4, 9, 12],
                [4, 7, 10, 13],
                [6, 8, 11, 15]
            ]

    print(find(0, array))