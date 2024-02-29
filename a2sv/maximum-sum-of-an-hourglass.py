class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        sumglass = [(0,0), (-1, -1), (-1, 0), (-1, 1), (1, 1), (1, 0), (1, -1)]
        max_total = 0
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                total_in = 0
                for x, y in sumglass:
                    total_in += grid[row + x][col + y]
                if total_in > max_total:
                    max_total = total_in

        return max_total
        
