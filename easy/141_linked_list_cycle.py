from typing import List


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next}"

    def new(l: List, pos):
        first = l.pop(0)
        r = ListNode(first)
        c = r
        c_pos = 0
        link = first
        while len(l) > 0:
            if c_pos == pos:
                link = c
            c_val = l.pop(0)
            c_ln = ListNode(c_val)
            c.next = c_ln
            c = c_ln
            c_pos += 1
        if pos != -1:
            c.next = link

        return r

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        c = head
        visited = {}
        while c is not None:
            if id(c) in visited:
                return True
            else:
                visited[id(c)] = True
                c = c.next
        return False

# print(ListNode.new([3,2,0,-4], 1))
s = Solution()
print(s.hasCycle(ListNode.new([3,2,0,-4], 1)))
print(s.hasCycle(ListNode.new([3,2,0,-4], -1)))
print(s.hasCycle(ListNode.new([1, 2], 0)))