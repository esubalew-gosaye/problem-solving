# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for i in range(len(logs)):
            if logs[i] == "../":
                if len(stack):
                    stack.pop()
            elif logs[i] != "./":
                stack.append(1)
        
        return len(stack)