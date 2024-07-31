# Problem: Maximum Element After Decreasing and Rearranging - https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        max_num = 1
        for i in  range(1, len(arr)): # [1, 100, 1000]
            if arr[i] > max_num:
                max_num += 1
        return max_num

            