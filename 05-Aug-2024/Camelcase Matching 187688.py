# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def solve(query,pattern):
            j = 0
            for i in range(len(query)):
                if j < len(pattern) and query[i] == pattern[j]:
                    j += 1
                elif query[i].isupper():
                    return False
            return j == len(pattern)

        return [solve(query, pattern) for query in queries]