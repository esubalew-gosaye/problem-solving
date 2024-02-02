class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        if x == 0: return True
        if x < 0:
            return False
        st = ""
        while x > 0:
            st += str(x % 10)
            x = x // 10
        return str(y) == st
