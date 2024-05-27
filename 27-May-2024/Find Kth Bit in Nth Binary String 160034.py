# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def recurs(n, s):
            if n == 0:
                return s[k - 1]
            
            return recurs(n - 1, "".join([s, '1', *['0' if i=='1' else '1' for i in s][::-1]]))
        
        return recurs(n, "0")