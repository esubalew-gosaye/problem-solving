# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                start = mid
                while 0 <= start and nums[start] == target:
                    start -= 1
                end = mid
                while end < n and nums[end] == target:
                    end += 1
                return [start + 1, end - 1]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return [-1, -1]