# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {}
        for person, judge in trust:
            trusts[judge] = trusts.get(judge, 0) + 1

        if n == 1:
            return n
        for key, value in trusts.items():
            if value == n-1:
                if not key in [i[0] for i in trust]:
                    return key 
       
        return -1
        
        

        