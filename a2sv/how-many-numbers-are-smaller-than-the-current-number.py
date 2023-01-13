class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            count = 0
            for i in nums:
                if num > i: count+=1
            arr+=[count]
        return arr
