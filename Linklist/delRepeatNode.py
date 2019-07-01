from Linklist import *

"""
给出一个有序链表，删除掉重复节点
"""


def delete_duplicates(head):
    if head is None or head.next is None:
        return head
    head.next = delete_duplicates(head.next)
    if head.val == head.next.val:
        return head.next
    else:
        return head


if __name__ == '__main__':
    head = build_l("5556")
    print_l(delete_duplicates(head))