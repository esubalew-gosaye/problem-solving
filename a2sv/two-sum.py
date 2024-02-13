class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num in enumerate(nums):
            target_2 = target - num
            if target_2 in store:
                return [i, store[target_2]]
            
            store[num] = i 
