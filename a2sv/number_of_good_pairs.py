class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(nums[i+1:].count(nums[i]) for i in range(len(nums)))
