# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0 for i in range(k)]
        self.minUnFair = float("inf")

        def backtrack(i):
            if i >= len(cookies):
                self.minUnFair = min(self.minUnFair, max(children))
                return
            
            currCookie = cookies[i]
            for child in range(len(children)):
                children[child] += currCookie
                if children[child] < self.minUnFair:
                    backtrack(i + 1)
                children[child] -= currCookie

        backtrack(0)

        return self.minUnFair
