# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        while k:
            _max = heapq.heappop(piles)
            _max //=2
            heappush(piles, _max)
            k -= 1
        return -sum(piles)