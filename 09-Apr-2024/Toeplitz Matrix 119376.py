# Problem: Toeplitz Matrix - https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        store = defaultdict(set)


        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                store[row - col].add(matrix[row][col])

        return all(len(store[key]) == 1 for key in store)