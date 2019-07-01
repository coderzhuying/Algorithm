from Tree import *
import queue


class Recursion:
    """
    递归前，中，后序遍历二叉树
    """
    def preorder(self, root):
        if root:
            print(root.val)
            self.preorder(root=root.left)
            self.preorder(root=root.right)

    def inorder(self, root):
        if root:
            self.inorder(root=root.left)
            print(root.val)
            self.inorder(root=root.right)

    def postorder(self, root):
        if root:
            self.postorder(root=root.left)
            self.postorder(root=root.right)
            print(root.val)


class NotRecursion:
    """
    非递归前，中，后序遍历二叉树
    """
    def preorder(self, root):
        stack = []
        p = root
        while p or stack:
            while p:
                print(p.val)
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                p = p.right

    def inorder(self, root):
        res = []
        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            if stack:
                p = stack.pop()
                res.append(p.val)
                p = p.right

        return res

    def postorder(self, root):
        stack = []
        p = root
        q = None
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:
                p = stack[-1]
                if p.right is None or p.right == q:
                    p = stack.pop()
                    print(p.val)
                    q = p
                    p = None
                else:
                    p = p.right


def levelOrder(root):
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        p = q.get()
        print(p.val)
        if p.left:
            q.put(p.left)
        if p.right:
            q.put(p.right)


def sumNode(root):
    """
    :param root: 二叉树的根节点
    :return: 二叉树共有多少个节点
    """
    if not root:
        return 0
    else:
        return 1 + sumNode(root.left) + sumNode(root.right)


def leafNode(root):
    """
    :param root: 二叉树的根节点
    :return: 打印叶子节点，返回叶子节点数目
    """
    if not root:
        return 0
    if not root.left and not root.right:
        print(root.val)
        return 1
    return leafNode(root.left)+leafNode(root.right)


def depth(root):
    """
    :param root: 二叉树的根
    :return:
    """
    if not root:
        return 0
    else:
        hl = depth(root.left)
        hr = depth(root.right)

    return (hl if hl > hr else hr) + 1


if __name__ == '__main__':
    root = construct_tree()
    # Re = Recursion()
    Re = NotRecursion()
    # Re.preorder(root)
    # print("*" * 20)
    print(Re.inorder(root))
    # print("*"*20)
    # Re.postorder(root)

    # levelOrder(root=root)
    # print(sumNode(root))
    # print(leafNode(root))
    print(depth(root))