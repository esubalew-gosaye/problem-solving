# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        result = [row[:] for row in mat]
        visited = set()
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    visited.add((i, j))
                    queue.append((i, j, 0))

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while queue:
            row, col, steps = queue.popleft()

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                if 0 <= next_row < m and 0 <= next_col < n and (next_row, next_col) not in visited:
                    result[next_row][next_col] = steps + 1
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))

        return result