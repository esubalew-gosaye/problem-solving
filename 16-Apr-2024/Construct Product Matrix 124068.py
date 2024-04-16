# Problem: Construct Product Matrix - https://leetcode.com/problems/construct-product-matrix/description/

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        prefix = [1]
        suffix = [1]

        for row in range(rows):
            for col in range(cols):
                prefix.append((prefix[-1] * grid[row][col]) % 12345)
                suffix.append((suffix[-1] * grid[rows - row - 1][cols - col - 1]) % 12345)

        suffix.reverse()

        ans = []
        tmp = []
        count = 0
        for i in range(1, rows * cols + 1):
            if count == cols:
                ans.append(tmp)
                tmp = []
                count = 0
            count += 1
            tmp.append((prefix[i - 1] * suffix[i]) % 12345)
        ans.append(tmp)
        
        return ans