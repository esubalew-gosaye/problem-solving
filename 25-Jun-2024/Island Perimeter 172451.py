# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        perimeter = 0

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        
        def dfs(row, col):
            nonlocal perimeter

            if grid[row][col]:
                sides = 4
                for x, y in directions:
                    if inbound(row + x, col + y) and  grid[row + x][col + y]:
                        sides -= 1
                perimeter += sides

            visited[row][col] = True

            for offsetX, offsetY in directions:
                x = row + offsetX
                y = col + offsetY 

                if inbound(x, y) and not visited[x][y]:
                    dfs(x, y)
                

        dfs(0, 0)

        return perimeter