# Problem: Sum of Distances - https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)
        left_sum = defaultdict(int)
        left_freq = defaultdict(int)
        for i, num in enumerate(nums):
            ans[i] += left_freq[num] * i
            ans[i] -= left_sum[num]

            left_sum[num] += i
            left_freq[num] += 1

        right_sum = defaultdict(int)
        right_freq = defaultdict(int)
        for i, num in reversed(list(enumerate(nums))):
            ans[i] -= right_freq[num] * i
            ans[i] += right_sum[num]

            right_sum[num] += i
            right_freq[num] += 1

        return ans