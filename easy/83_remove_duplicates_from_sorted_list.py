from typing import Optional, List


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next}"

    def new(l: List):
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        c = head
        while c is not None:
            if c.next is None:
                break
            if c.val == c.next.val:
                c.next = c.next.next
            else:
                c = c.next
        return head


s = Solution()
print(s.deleteDuplicates(ListNode.new([1, 1, 2])))
print(s.deleteDuplicates(ListNode.new([1,1,2,3,3])))
print(s.deleteDuplicates(ListNode.new([1,1,1])))