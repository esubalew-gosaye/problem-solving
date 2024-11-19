# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in numSet:
            if not num - 1 in numSet:
                cnt = 1
                while num + cnt in numSet:
                    cnt += 1
                longest = max(longest, cnt)
        return longest