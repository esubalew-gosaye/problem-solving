# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {}

        def dfs(remaining):
            if remaining < 0:
                return float('inf')
            if remaining == 0:
                return 0
            if remaining in dp:
                return dp[remaining]
            
            min_coins = float('inf')
            for coin in coins:
                res = dfs(remaining - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, 1 + res)
            
            dp[remaining] = min_coins
            return dp[remaining]

        result = dfs(amount)
        return -1 if result == float('inf') else result