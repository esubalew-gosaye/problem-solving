# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if mid != n - 1 and not isBadVersion(mid) and isBadVersion(mid + 1):
                return mid + 1
            elif isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return n
            