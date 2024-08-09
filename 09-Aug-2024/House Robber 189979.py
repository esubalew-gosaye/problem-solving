# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0

        for money in nums:
            temp = max(first + money, second)
            first = second
            second = temp
            
        return second