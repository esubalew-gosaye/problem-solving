# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"{":"}", "(":")", "[":"]"}

        for char in s:
            if char in brackets.keys():
                stack.append(char)
            else:
                if stack == []:
                    return False
                    
                closing_bracket = stack.pop()
                if char != brackets[closing_bracket]:
                    return False                    
                
        return stack == []