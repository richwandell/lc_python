
from typing import Optional, List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{" + f"{self.left} {self.val} {self.right}" + "}"

    def new(l: List):
        val = l.pop(0)
        r = TreeNode(val)
        nodes = [r]

        while len(l) > 0:
            node = nodes.pop(0)
            if len(l) > 0:
                val = l.pop(0)
                if val:
                    node.left = TreeNode(val)
                    nodes.append(node.left)
            if len(l) > 0:
                val = l.pop(0)
                if val:
                    node.right = TreeNode(val)
                    nodes.append(node.right)
        return r


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: return True
        if p is None: return False
        if q is None: return False

        p_stack, q_stack = [p], [q]

        while len(p_stack) + len(q_stack) > 0:
            p_item, q_item = p_stack.pop(), q_stack.pop()
            if p_item.val != q_item.val: return False
            if (p_item.left and not q_item.left) or (q_item.left and not p_item.left) : return False
            if (p_item.right and not q_item.right) or (q_item.right and not p_item.right): return False

            if p_item.left and q_item.left:
                p_stack.append(p_item.left)
                q_stack.append(q_item.left)
            if p_item.right and q_item.right:
                p_stack.append(p_item.right)
                q_stack.append(q_item.right)
        return True

s = Solution()
print(s.isSameTree(TreeNode.new([1,2,3]), TreeNode.new([1,2,3])))
print(s.isSameTree(TreeNode.new([1,2]), TreeNode.new([1,None,2])))
print(s.isSameTree(TreeNode.new([1,2,1]), TreeNode.new([1,1,2])))