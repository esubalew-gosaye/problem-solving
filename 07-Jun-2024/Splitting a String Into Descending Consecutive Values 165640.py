# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        curr = []

        def backtrack(s):
            if not s:
                return len(curr) > 1
            
            for i in range(len(s)):
                left = s[:i+1]
                right = s[i+1:]
                if not curr or curr[-1] - int(left) == 1:
                    curr.append(int(left))
                    if backtrack(right):
                        return True 
                    
                    curr.pop()
            
            return False

        return backtrack(s)