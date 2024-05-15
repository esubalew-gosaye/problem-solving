# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def find(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.ans.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.find(root)
        return self.ans