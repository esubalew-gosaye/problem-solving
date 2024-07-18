# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)
        res = 0
        i = 0
        count = 0
        sub = 0
        while count < k:
            if happiness[i] - sub > 0:
                res += happiness[i] - sub
            sub += 1
            i += 1
            count += 1
        return res