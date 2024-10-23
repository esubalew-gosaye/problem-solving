# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = float("-inf")
        mn = float("inf")

        for i in nums:
            mx = max(mx, i)
            mn = min(mn, i)
        for j in range(mn, 0, -1):
            if mx % j == mn % j == 0:
                return j