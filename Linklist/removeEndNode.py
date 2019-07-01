from Linklist import *

"""
删除链表倒数第n个节点
"""


def remove(head, n):
    slow = fast = head
    i = 0
    while i < n:
        fast = fast.next
        i = i + 1

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return head


if __name__ == '__main__':
    head = build_l("12345")
    print_l(remove(head, 2))