# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, num: List[int]) -> List[int]:
        length = len(num)
        if length == 1:
            return num

        left = self.sortArray(num[:length // 2])
        right = self.sortArray(num[length // 2:])

        return self.merge(left, right, num)

    def merge(self, left, right, num):
        l, r, i = 0, 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                num[i] = left[l]
                l += 1
            else:
                num[i] = right[r]
                r += 1
            i += 1
            
        while l < len(left):
            num[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            num[i] = right[r]
            r += 1
            i += 1

        return num

        
        

        