# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weights = weights[0]
        sum_weights = 0
        for weight in weights:
            sum_weights += weight
            if weight > max_weights: 
                max_weights = weight

        def find_days(capacity):
            day = 1
            total = 0
            for i in range(0, len(weights)):
                if total + weights[i] <= capacity:
                    total += weights[i]
                else:
                    day += 1
                    total = weights[i]
            
                if day > days: return False
            return True 

        low = max_weights
        high = sum_weights
        while low <= high:
            mid = (low + high) // 2

            if find_days(mid):
                high = mid - 1
            else:
                low = mid + 1
                
        return low