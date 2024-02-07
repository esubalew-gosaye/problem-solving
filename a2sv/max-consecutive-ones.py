class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        list_count = []
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                list_count.append(count)
                count = 0
        list_count.append(count)
        return max(list_count)

        
