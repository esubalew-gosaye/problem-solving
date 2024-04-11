# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        num_elements = len(mat) * len(mat[0])

        rows = len(mat)
        cols = len(mat[0])

        row = 0
        col = 0

        store = defaultdict(list)

        for row in range(rows):
            for col in range(cols):
                store[row + col].append(mat[row][col])
            
            
        ans = []
        for key in store:
            if key % 2 == 0:
                for elm in range(len(store[key])-1, -1, -1):
                    ans.append(store[key][elm])
            else:
                for elm in range(len(store[key])):
                    ans.append(store[key][elm])
        return ans