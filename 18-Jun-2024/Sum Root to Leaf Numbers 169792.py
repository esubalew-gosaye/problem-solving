# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        store = []
        ans = 0

        def backtrack(root):
            nonlocal ans
            
            if not root.left and not root.right:
                store.append(str(root.val))
                ans += int("".join(store))
                store.pop()
                
                return
            
            store.append(str(root.val))

            if root.left:
                backtrack(root.left)
            
            if root.right:
                backtrack(root.right)

            store.pop()

        backtrack(root)

        return ans


