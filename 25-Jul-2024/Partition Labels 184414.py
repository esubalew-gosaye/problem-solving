# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        stats = {val: index for index, val in enumerate(s)}

        ans = []
        _min = 0
        _max = 0
        
        for i in range(len(s)):
            _max = max(_max, stats[s[i]])

            if _max == i:
                ans.append(_max - _min + 1)
                _min = _max + 1
                
        return ans