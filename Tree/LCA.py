from Tree import *
"""
二叉树/二叉搜索树的最近公共祖先
"""


def lca_BT(root, p, q):
    """
    二叉树的最近公共祖先
    思路：递归查找,如果在左子树为空说明,q和p都在右子树,最近公共祖先也在左子树,右子树同理
    :param root:
    :param p:
    :param q:
    :return:
    """
    if root is None:                    # 如果根为空，返回空
        return root
    if root.val == p or root.val == q:  # root如果等于p或q，说明最近公共祖先就是p或q
        return root.val
    left = lca_BT(root.left, p, q)      # 递归找左子树和右子树
    right = lca_BT(root.right, p, q)
    if left is None:
        return right
    elif right is None:
        return left
    else:
        return root.val


def lca_BST(root, p, q):
    """
    二叉搜索树的最近公共祖先
    思路：递归查找,如果在左子树为空说明,q和p都在右子树,最近公共祖先也在左子树,右子树同理,此时只需要比较val即可
    :param root:
    :param p:
    :param q:
    :return:
    """
    if p < root.val > q:            # 如果p和q都小于root，说明p和q在左子树
        return lca_BST(root.left, p, q)
    if p > root.val < q:            # 如果p和q都大于root，说明p和q在右子树
        return lca_BST(root.right, p, q)
    return root.val


def no_re_lac_BST(root, p, q):
    """
    二叉搜索树的最近公共祖先,非递归
    :param root:
    :param p:
    :param q:
    :return:
    """
    while root:
        if p < root.val > q:
            root = root.left
        elif p > root.val < q:
            root = root.right
        else:
            return root.val


if __name__ == "__main__":
    root = construct_tree()
    print(lca_BT(root, 2, 4))
    print(lca_BST(root, 2, 4))
    print(no_re_lac_BST(root, 2, 4))