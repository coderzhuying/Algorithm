from Tree import *
"""
验证二叉搜索树
"""


def isValidBST(root):
    inorder_list = inorder(root)
    return inorder_list == list(sorted(set(inorder_list)))


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def isValid(root, min, max):
    if root is None:
        return True
    if min and root.val <= min:
        return False
    if max and root.val >= max:
        return False

    return isValid(root.left, min, root.val) and isValid(root.right, root.val, max)


if __name__ == "__main__":
    root = construct_tree()
    print(isValid(root, min=None, max=None))
    print(isValidBST(root))