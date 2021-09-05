from typing import Optional

from helpers.ListNode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node):
            if node is None or node.next is None:
                return node
            n = reverse(node.next)
            node.next.next = node
            node.next = None
            return n

        return reverse(head)

s = Solution()
print(s.reverseList(ListNode.new([1, 2, 3, 4, 5])).print())
