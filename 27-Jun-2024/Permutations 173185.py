# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        current = []
        def backtrack():
            if len(current) == len(nums):
                ans.append(current[:])
                return
            
            for i in range(len(nums)):
                if not nums[i] in current:
                    current.append(nums[i])
                    backtrack()
                    current.pop()
        
        backtrack()

        return ans