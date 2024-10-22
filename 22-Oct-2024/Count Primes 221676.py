# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        primes = [True for i in range(n)]
        
        primes[0] = False
        primes[1] = False

        j = 2 
        while j < n ** .5:
            if primes[j]:
                for k in range(j, n, j):
                    if k == j: continue
                    primes[k] = False
            j += 1 
        return sum(primes)
        

