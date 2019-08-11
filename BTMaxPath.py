from Tree import *


class Solution():
    """
    二叉树最长路径
    """
    def main(self, root):
        self.ans = 0
        def getHeight(root):
            if root is None:
                return 0
            l = getHeight(root.left)
            r = getHeight(root.right)
            self.ans = max(self.ans, l+r+1)
            return max(l, r) + 1
        getHeight(root)
        return self.ans


if __name__ == '__main__':
    root = construct_tree()
    s = Solution()
    print(s.main(root))
