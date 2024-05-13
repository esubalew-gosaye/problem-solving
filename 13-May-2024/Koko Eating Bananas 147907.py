# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
       
        def find_k(k):
            total = 0
            for i in range(0, n):
                total += ceil(piles[i] / k) 
                if total > h: return False
            return True 

        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2

            if find_k(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low