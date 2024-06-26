# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        totalSum = 0

        def dfs(node, parent):
            nonlocal totalSum

            if not node:
                return

            if len(parent) >= 2 and parent[-2] % 2 == 0:
                totalSum += node.val
            
            if node.right:
                dfs(node.right, parent + [node.val])

            if node.left:
                dfs(node.left, parent + [node.val])

        dfs(root, [])

        return totalSum