# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        store = {}
        stack = []
        for num in nums2:

            while stack and stack[-1] < num:
                store[stack.pop()] = num
            stack.append(num)
            
        print(store)
        return [store.get(i, -1) for i in nums1]