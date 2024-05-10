# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def dfs(i, j):
            if i == j:
                return nums[i]
            leftDiff = nums[i] - dfs(i + 1, j)
            rightDiff = nums[j] - dfs(i, j - 1)
            return max(leftDiff, rightDiff)
        
        return dfs(0, n - 1) >= 0
        