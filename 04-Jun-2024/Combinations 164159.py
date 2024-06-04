# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combinations = []
        cur = []

        def backtrack(num):
            if len(cur) == k:
                combinations.append(cur[:])
                return
            
            for num_ in range(num, n + 1):
                cur.append(num_)
                backtrack(num_ + 1)
                cur.pop()
            
        backtrack(1)
        return combinations