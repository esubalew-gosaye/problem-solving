# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        if not root:
            return ans

        queue = deque([root])

        while queue:
            N = len(queue)
            sameLevel = []

            for _ in range(N):
                node = queue.popleft()
                sameLevel.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            ans.append(sameLevel.copy())
            sameLevel = []
        return ans

            

            
