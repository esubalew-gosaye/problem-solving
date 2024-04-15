# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        prefix = [0]
        for i in range(len(cardPoints)):
            prefix.append(prefix[-1] + cardPoints[i])

        ans = 0
        for j in range(k + 1):
            ans = max(ans, prefix[j] + prefix[-1] - prefix[n - k + j])

        return ans