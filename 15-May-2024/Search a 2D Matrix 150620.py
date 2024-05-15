# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def check_in_row(row):
            print(target, row)
            low = 0
            high = len(row) - 1

            while low <= high:
                mid = (low + high) // 2
                if row[mid] == target:
                    return True
                elif target > row[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        for row in matrix:
            print(row[-1])
            if row[-1] == target:
                return True
            elif row[-1] > target:
                return check_in_row(row)
        return False  