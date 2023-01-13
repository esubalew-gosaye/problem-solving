class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ls = []
        for i in range(len(nums)):
            if nums[i] == target: ls+=[i]
        return ls
