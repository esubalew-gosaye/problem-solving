# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        offSet = 1

        for i in range(1, n + 1):
            if offSet * 2 == i:
                offSet *= 2
            ans[i] = ans[i - offSet] + 1
        
        return ans
