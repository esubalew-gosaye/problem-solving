# Problem: Score of parenthesis - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        closing = 0
        full = 0
        ans = 0

        for char in s+"(":
            if char == "(":
                if full !=0 :
                    val = 2**(full-1)
                    closing -= full
                    ans += 2**closing * val
                    full = 0
                closing += 1
            else:
                full += 1

        return ans
