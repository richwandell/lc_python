from typing import List


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        try:
            return f"{self.val} {self.next.print() if self.next else ''}"
        except Exception:
            return str(self)

    def new(l: List, pos=-1):
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