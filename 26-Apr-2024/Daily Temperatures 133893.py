# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        stack = []

        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                popItem, popInd = stack.pop()
                ans[popInd] = ind - popInd

            stack.append((temp, ind))
        
        return ans

        