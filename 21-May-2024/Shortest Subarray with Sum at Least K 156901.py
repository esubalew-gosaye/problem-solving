# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque([(0, -1)])
        running_sum = 0
        maxLen = float('inf')

        for i in range(len(nums)):
            running_sum += nums[i]

            while queue and queue[-1][0] >= running_sum:
                queue.pop()

            queue.append((running_sum, i))

            start, end = queue[0][0], queue[-1][0]

            while end - start >= k:
                _, idx = queue.popleft()
                maxLen = min(maxLen, i - idx)
                start = queue[0][0]
            
        return -1 if float('inf') == maxLen else maxLen

            
