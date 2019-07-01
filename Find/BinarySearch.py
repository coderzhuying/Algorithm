"""
二分查找
recursion: 递归函数，查找是否存在
binarySearch: 封装递归函数
              如果查找存在返回下标
              如果不存在返回-1
"""


def recursion(target, small, big, args):
    mid = int((small+big)/2)
    if args[mid] == target:
        # print(args[mid], target)
        return mid
    elif args[mid] > target:
        return recursion(target, small, mid+1, args)
    else:
        return recursion(target, mid+1, big, args)


def binarySearch(target, args):
    index = len(args)
    try:
        result = recursion(target, 0, index - 1, args)
    except:
        return -1
    else:
        return result


def BS(target, array):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    print(binarySearch(3,[1,2,3,4,5,6]))
    print(BS(3,[1,2,3,4,5,6]))




