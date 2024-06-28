# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        freshOrange = 0
        queue = deque()
        time = 0

        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 2:
                    queue.append((i, j))
                
                if grid[i][j] == 1:
                    freshOrange += 1

        while queue and freshOrange > 0:
            N = len(queue)
            for _ in range(N):
                X, Y = queue.popleft()
                for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    if inbound(x + X, y + Y) and grid[x + X][y + Y] == 1:
                        grid[x + X][y + Y] = 2
                        queue.append((x + X, y + Y))
                        freshOrange -= 1

            time += 1
            
        return -1 if freshOrange else time
        