# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Linklist import build_l, print_l

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储 一位数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：807
"""
def addTwoNumbers(l1, l2):
    i = j = 0
    sum = 0
    b = 0
    while l1 or l2:
        if l1 and l2:
            v1 = l1.val
            v2 = l2.val
            sum += ((v1 + v2 + b) % 10) * pow(10, i)
            # print((v1 + v2 + b) % 10)
            b = int((v1 + v2 + b) / 10)
            i += 1
            j += 1
            l1 = l1.next
            l2 = l2.next
        elif l1:
            v1 = l1.val
            sum += ((v1 + b) % 10) * pow(10, i)
            b = int((v1 + b) / 10)
            print(((v1 + b) % 10))
            i += 1
            l1 = l1.next
        else:
            v2 = l2.val
            sum += ((v2 + b) % 10) * pow(10, j)
            b = int((v2 + b) / 10)
            j += 1
            l2 = l2.next

    if b != 0:
        sum += b * pow(10, max([i, j]))

    return sum

head1 = build_l([3, 8, 4])
head2 = build_l([2, 4, 5])
print_l(head2, "SINGLE")

print(addTwoNumbers(head1, head2))