# Definition for a binary tree node.
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def in_order(tree: TreeNode):
            if tree.left is None and tree.right is not None:
                return [tree.val] + in_order(tree.right)
            elif tree.right is None and tree.left is not None:
                return in_order(tree.left) + [tree.val]
            elif tree.right is None and tree.left is None:
                return [tree.val]
            return in_order(tree.left) + [tree.val] + in_order(tree.right)

        return in_order(root)

# print(TreeNode.new([1, 2, 3, 4, 5]))
# print(TreeNode.new([1, None, 2, 3]))
s = Solution()
# print(s.inorderTraversal(TreeNode.new([1, None, 2, 3])))
print(s.inorderTraversal(TreeNode.new([1, 2, 3, 4, 5])))