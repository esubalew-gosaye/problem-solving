# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid) -> int:
        
        islands = 0
        visited  = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            for X, Y in directions:
                offset_X = X + x
                offset_Y = Y + y
                if 0 <= offset_X < len(grid) and 0 <= offset_Y < len(grid[0]) and grid[offset_X][offset_Y] == "1" and not (offset_X, offset_Y) in visited:
                    visited.add((x + X, y + Y))
                    dfs(x + X, y + Y)
                    
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not (i, j) in visited:
                    dfs(i, j)
                    visited.add((i, j))
                    islands += 1
        return islands