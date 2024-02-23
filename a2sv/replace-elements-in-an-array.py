class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        ls = dict()

        for i in range(len(nums)):
            ls[nums[i]] = i
        
        for elm, rep in operations:
            index = ls.pop(elm)
            ls[rep] = index

        for j in ls:
            nums[ls[j]] = j
        
        return nums
