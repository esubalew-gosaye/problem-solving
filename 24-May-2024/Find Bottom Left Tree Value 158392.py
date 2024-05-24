# Problem: Find Bottom Left Tree Value - https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         val = val
#         left = left
#         right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        maxDepth = -1
        leftVal = 0
        lvl = 0

        def travs(root, lvl):
            nonlocal maxDepth, leftVal
            if not root:
                return

            if lvl > maxDepth:
                maxDepth = lvl
                leftVal = root.val

            travs(root.left, lvl + 1)
            travs(root.right, lvl + 1)

        travs(root, 0)
        return leftVal