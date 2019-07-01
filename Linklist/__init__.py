class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def build_l(nums):
    head = ListNode(nums[0])
    cur = head
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head


# 三种打印链表的形式, 字符串, ->, 列表
def print_l(head, p_type="SINGLE"):
    p = head
    result = []
    while p:
        if p_type in ["STR", "SINGLE"]:
            result.append(str(p.val))
        else:
            result.append(p.val)
        p = p.next
    if p_type == "STR":
        print(" ".join(result))
    elif p_type == "LIST":
        print(result)
    elif p_type == "SINGLE":
        print(" -> ".join(result))
    else:
        print("error dType!!!")


if __name__ == '__main__':
    nums1 = "hello"
    head1 = build_l(nums1)
    print_l(head1, "SINGLE")