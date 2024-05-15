# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        # arr = [(1, 2), (2, 1), (3, 0)]
        # intervals = [[1,4],[2,3],[3,4]]

        arr = []
        n = len(intervals)
        for i in range(n):
            arr.append((intervals[i][0], i))
        arr.sort()
        
        ans = []
        for intv in intervals:

            low = 0
            high = n - 1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid][0] < intv[1]:
                    low = mid + 1 
                else:
                    high = mid - 1

            ans.append(arr[low][1] if low <= n - 1 and arr[low][0] >= intv[1] else -1)

        return ans






