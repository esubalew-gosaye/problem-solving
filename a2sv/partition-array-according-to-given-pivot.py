class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_element = []
        left_element = []
        right_element = []

        for num in nums:
            if num == pivot:
                pivot_element.append(num)
            elif num > pivot:
                right_element.append(num)
            else:
                left_element.append(num)
        return left_element + pivot_element + right_element
        
