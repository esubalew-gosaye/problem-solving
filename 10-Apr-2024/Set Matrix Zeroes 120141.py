# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_row = len(matrix)
        len_col = len(matrix[0])
        list_of_zero = []

        for row in range(len_row):
            for col in range(len_col):
                if matrix[row][col] == 0:
                    list_of_zero.append(row * len_col + col)

        for point in list_of_zero:
            row = point // len_col
            col = point % len_col

            for j in range(len_col):
                matrix[row][j] = 0
            for k in range(len_row):
                matrix[k][col] = 0
