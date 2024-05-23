# Problem: Maximum Width of Binary Tree - https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = []

        def width(root, lvl, num):
            if not root:
                return
            
            if lvl >= len(level):
                level.append([num, num])
            else:
                level[lvl][0] = min(level[lvl][0], num)
                level[lvl][1] = max(level[lvl][1], num)

            width(root.left, lvl + 1, num * 2 - 1)
            width(root.right, lvl + 1, num * 2)

        width(root, 0, 1)

        maxWidth = 0
        for left, right in level:
            maxWidth = max(maxWidth, right - left + 1)
        
        return maxWidth