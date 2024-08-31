# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = str(bin(n))
        for i in range(len(bin(n))-1):
            if s[i]==s[i+1]:
                return False
        return True