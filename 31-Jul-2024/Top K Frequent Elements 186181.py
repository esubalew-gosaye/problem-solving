# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        item = Counter(nums)
        return heapq.nlargest(k, Counter(nums), key=lambda x: item[x])