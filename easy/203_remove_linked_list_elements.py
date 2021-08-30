from typing import Optional, List

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next}"

    def new(l: List):
        if len(l) == 0:
            return None
        first = l.pop(0)
        r = ListNode(first)
        c = r
        while len(l) > 0:
            c_val = l.pop(0)
            c_ln = ListNode(c_val)
            c.next = c_ln
            c = c_ln
        return r


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        c, p = head, head

        while c is not None:
            if c.val == val:
                p.next = c.next
                c = c.next
                continue
            p = c
            c = c.next
        if head and head.val == val:
            return head.next
        return head


s = Solution()
print(s.removeElements(ListNode.new([1,2,6,3,4,5,6]), 6))
print(s.removeElements(ListNode.new([]), 7))
print(s.removeElements(ListNode.new([7,7,7,7]), 7))
print(s.removeElements(ListNode.new([1,2,2,1]), 2))