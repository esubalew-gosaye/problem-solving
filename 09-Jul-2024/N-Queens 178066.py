# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        posDiagonal = set()
        negDiagonal = set()

        def backtrack(row):
            if row == n:
                ans.append(["".join(rw) for rw in board])
                return

            for col in range(n):
                if col in cols or (col + row) in posDiagonal or (row - col) in negDiagonal:
                    continue
                cols.add(col)
                posDiagonal.add(col + row)
                negDiagonal.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                posDiagonal.remove(col + row)
                negDiagonal.remove(row - col)
                board[row][col] = "."
        

        backtrack(0)
        return ans