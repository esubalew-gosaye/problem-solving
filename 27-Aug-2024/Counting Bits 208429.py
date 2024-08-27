# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [-1]*(n+1)
        dp[0] = 0
        for num in range(1,n+1):
            q, r = divmod (num, 2)
            dp [num] = r + dp[q]
        return dp