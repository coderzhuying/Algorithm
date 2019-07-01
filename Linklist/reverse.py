from Linklist import *

"""
逆置链表
"""


def reverse_list(head):
    cur = head
    prev = ListNode(-1)

    while cur:
        # cur.next, prev, cur = prev, cur, cur.next
        temp = cur
        prev.next = cur
        cur.next = prev.next
        cur = temp.next
    return prev.next


if __name__ == '__main__':
    head = build_l("12345")
    print_l(reverse_list(head))