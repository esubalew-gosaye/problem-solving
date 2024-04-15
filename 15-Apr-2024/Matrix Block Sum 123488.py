# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        def validate(val, d):
            if val <= 0:
                return 0
            if d == 1 and val >= cols:
                return cols - 1
            if d == 0 and val >= rows:
                return rows - 1
            return val

        ans = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                sm = 0
                for r in range(validate(row - k, 0), validate(row + k, 0) + 1):
                    for c in range( validate(col - k, 1), validate(col + k, 1) + 1):
                        sm += mat[r][c]
                
                tmp.append(sm)
            ans.append(tmp)
            
        return ans