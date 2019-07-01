from Linklist import *

"""
链表交换相邻节点
"""

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next is not None and pre.next.next is not None:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a

        return self.next


def swap(head):
    p = ListNode(None)
    pre = p
    pre.next = head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a

    return p.next


if __name__ == '__main__':
    head = build_l("12345")
    print_l(swap(head))

