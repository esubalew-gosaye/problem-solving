# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        low = 0
        high = n - 1

        if n == 1 or nums[0] <= nums[-1]:
            return nums[0]

        while low < high:

            mid = (high + low) // 2

            if nums[mid] >= nums[0]:
                low = mid + 1

            else:
                high = mid

        return nums[low]

          
