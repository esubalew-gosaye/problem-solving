# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes >= k:
            return k

        k -= numOnes

        if numZeros >= k:
            return numOnes

        k -= numZeros

        return numOnes + (-1 * k)