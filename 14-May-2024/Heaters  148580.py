# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(heaters)
        houses.sort()
        heaters.sort()
        radius = 0
        i = 0
        for house in houses:
            while i < n - 1 and heaters[i] <= house:
                i += 1

            left = abs(house - (heaters[i - 1]))
            right = abs(heaters[i] - house)
            radius = max(radius, min(left, right))

        return radius
