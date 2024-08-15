# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change (self, amount: int, coins: List[int]):
        last_level =  len(coins)
        
        @cache
        def solve(amount=amount, i=0):
            if i == last_level:
                return 0
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            return solve(amount-coins[i], i) + solve(amount,i+1)
            
        return solve()

        
            