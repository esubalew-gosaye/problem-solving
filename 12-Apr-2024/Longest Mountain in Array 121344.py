# Problem: Longest Mountain in Array - https://leetcode.com/problems/longest-mountain-in-array/

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        mount = 0
        left = 0
        right = 0
        for i in range(1, n):

            l = r = i
            while l > 0 and  arr[l - 1] <  arr[l]:
                l -= 1
            while n - 1 > r and  arr[r + 1] <  arr[r]:
                r += 1

            if i - l and r - i:
                mount = max(mount, r - l + 1)
            

        return mount