# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxNode = 0

        def travs(root, nd_min, nd_max):

            if not root:
                return nd_max - nd_min
            
            nd_min = min(nd_min, root.val)
            nd_max = max(nd_max, root.val)

            left = travs(root.left, nd_min, nd_max)
            right = travs(root.right, nd_min, nd_max)

            return max(right, left)
        
        return travs(root, root.val, root.val)