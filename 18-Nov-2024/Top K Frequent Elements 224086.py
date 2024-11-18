# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_freq = {}
        for i in nums:
            count_freq[i] = 1 + count_freq.get(i, 0)

        count_sort = [[] for i in range(len(nums) + 1)]
        for key, value in count_freq.items():
            count_sort[value].append(key)
        
        print(count_sort)
        ans = []
        for j in range(len(nums), 0, -1):
            if len(ans) == k:
                return ans
    
            ans.extend(count_sort[j])

        return ans
