# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        current = head

        while l1 is not None and l2 is not None:
            if l1 is None:
                current.next = l2.next
                l2 = l2.next
            elif l2 is None:
                current.next = l1.next
                l1 = l1.next
            elif l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        return head.next


l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
s = Solution()
print(s.mergeTwoLists(l1, l2))

















































# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#
#         d = ListNode(-1)
#         h = d
#         while l1 is not None or l2 is not None:
#             if l1 is None:
#                 d.next = l2
#                 l2 = l2.next
#             elif l2 is None:
#                 d.next = l1
#                 l1 = l1.next
#             elif l1.val > l2.val:
#                 d.next = l2
#                 l2 = l2.next
#             else:
#                 d.next = l1
#                 l1 = l1.next
#             d = d.next
#         return h.next
#
#
#
# l1 = ListNode(1, ListNode(2, ListNode(3)))
# l2 = ListNode(1, ListNode(3, ListNode(4)))
# s = Solution()
# print(s.mergeTwoLists(l1, l2))