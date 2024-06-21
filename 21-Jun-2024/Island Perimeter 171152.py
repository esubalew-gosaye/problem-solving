# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def check(i, j):
            neighbour = 0
            for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newX = x + i
                newY = y + j
                
                if newX < 0 or newY < 0 or newX >= row or newY >= col:
                    neighbour += 1
                elif grid[newX][newY] == 0:
                    neighbour += 1
                
            return neighbour

        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    perimeter += check(i, j)
        return perimeter

