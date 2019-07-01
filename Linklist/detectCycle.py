from Linklist import *

"""
判断一个链表是否有环
"""


def hasCycle(head):
    slow = fast = head
    while slow and fast and fast.next:
        if slow is fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False


if __name__ == '__main__':
    head = build_l("12")
    print(hasCycle(head))


