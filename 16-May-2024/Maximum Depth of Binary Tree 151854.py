# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depth = 0
        self.count = 0

    def maxDepths(self, root: Optional[TreeNode]) -> int:
        if root:
            self.count += 1
            self.maxDepths(root.left)
            self.depth = max(self.depth, self.count)
            self.maxDepths(root.right)

            self.count -= 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepths(root)
        return self.depth
        