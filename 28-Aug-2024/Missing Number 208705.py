# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(0, len(nums) + 1)) - set(nums)).pop()