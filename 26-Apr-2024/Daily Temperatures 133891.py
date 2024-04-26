# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        ans = {}

        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                ans[stack.pop()] = (temp, ind)

            stack.append((temp, ind))
        
        return [ans.get((temp, ind), (0, ind))[-1] - ind for ind, temp in enumerate(temperatures)]

        