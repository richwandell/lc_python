class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        l1v, l2v = "", ""
        l1c, l2c = l1, l2
        while l1c is not None or l2c is not None:
            if l1c is not None and l1c.val is not None:
                l1v = str(l1c.val) + l1v
                l1c = l1c.next
            if l2c is not None and l2c.val is not None:
                l2v = str(l2c.val) + l2v
                l2c = l2c.next
        result = str(int(l1v) + int(l2v))

        rlist = ListNode(False)
        first = rlist
        for i in range(len(result) - 1, -1, -1):
            num = result[i]
            rlist.val = num
            if i >= 1:
                rlist.next = ListNode(False)
                rlist = rlist.next
        return first





# ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
#
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
#
l1 = ListNode(1)
l1.next = ListNode(8)

l2 = ListNode(0)

s = Solution()
print(s.addTwoNumbers(l1, l2))