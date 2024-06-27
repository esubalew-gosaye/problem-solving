# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def backtrack(current, popped):
            if len(current) == 0:
                ans.append(popped[:])
                return
        
            for i in range(len(current)):
                num = current.pop(0)
                popped.append(num)
                backtrack(current, popped)
                current.append(num)
                popped.pop()
        
        backtrack(nums, [])

        return ans