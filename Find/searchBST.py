from Tree import *


def search(root, target):
    """
    :param root: 二叉搜索树
    :param target: 目标数
    :return: 找到返回True，否则返回False
    """
    if not root:
        return False
    if root.val == target:
        return True
    elif root.val > target:
        return search(root.left, target)
    else:
        return search(root.right, target)


if __name__ == '__main__':
    root = construct_tree()
    print(search(root, 8))