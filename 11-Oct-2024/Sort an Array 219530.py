# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_num = nums[0]
        min_num = nums[0]

        for num in nums:
            max_num = max(max_num, num)
            min_num = min(min_num, num)

        k = max_num - min_num
        arr = [0] * (k + 1)

        for num in nums:
            arr[num - min_num] += 1

        ind = 0

        for i in range(k + 1):
            while arr[i] > 0:
                nums[ind] = min_num + i
                ind += 1
                arr[i] -= 1
        return nums

        

        