# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        minQueue = deque()
        maxQueue = deque()

        for i in range(len(nums)):
            while minQueue and nums[minQueue[-1]] >= nums[i]:
                minQueue.pop()
            minQueue.append(i)

            while maxQueue and nums[maxQueue[-1]] <= nums[i]:
                maxQueue.pop()
            maxQueue.append(i)
            
            # max 5 4 4
            # min 2 4

            while nums[maxQueue[0]] - nums[minQueue[0]] > 2:
                if left == maxQueue[0]:
                    maxQueue.popleft()

                if left == minQueue[0]:
                    minQueue.popleft()
                
                left += 1
            
            ans += (i - left + 1)
        
        return ans

