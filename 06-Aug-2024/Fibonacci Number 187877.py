# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def __init__(self):
        self.memo = [0 for _ in range(31)]

    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        if self.memo[n]:
            return self.memo[n]
        
        val = self.fib(n - 1) + self.fib(n - 2)
        self.memo[n] = val
        return val