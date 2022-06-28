# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMaxDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left_length = self.findMaxDepth(root.left)
        right_length = self.findMaxDepth(root.right)

        return max(left_length, right_length) + 1

    def maxDepth(self, root: TreeNode) -> int:
        return self.findMaxDepth(root)
