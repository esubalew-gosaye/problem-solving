class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = []
        for row in range(len(matrix[0])):
            transpose = []
            for col in range(len(matrix)):
                transpose.append(matrix[col][row])
            new_matrix.append(transpose)
        return new_matrix
