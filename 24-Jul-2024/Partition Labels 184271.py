# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        stats = {}
        for index, val in enumerate(s):
            if val in stats:
                stats[val] = [stats[val][0], index]
            else:
                stats[val] = [index, index]

        ans = []
        _min = 0
        _max = stats[s[0]][1]
        indx = 0
        
        for i in range(1, len(s)):
            if s[indx] == s[i]:
                continue
            indx = i
            if stats[s[i]][0] > _max:
                ans.append(_max - _min + 1)
                _min = stats[s[i]][0]
                _max = stats[s[i]][1]

            if stats[s[i]][1] > _max:
                _max = stats[s[i]][1]
                
        ans.append(_max - _min + 1)
        return ans