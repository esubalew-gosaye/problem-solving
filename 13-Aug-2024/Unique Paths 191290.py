# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp (cell):
            row , col = cell
            if cell == (m-1 , n-1):
                return 1
            unique_ways = 0
            if row + 1 < m:
                unique_ways +=dp((row + 1,col))
            if col + 1 < n:
                unique_ways +=dp((row ,col + 1))
            return unique_ways 
        
        return dp((0,0))
        