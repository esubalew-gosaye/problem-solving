# Problem: Corporate Flight Bookings - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        ans = [0] * n

        for book in bookings:
            ans[book[0] - 1] = ans[book[0] - 1] + book[2]
            if book[1] < n:
                ans[book[1]] = -1 * book[2] + ans[book[1]]

        prefix_sum = [ans[0]]
        for i in range(1, n):
            prefix_sum.append(prefix_sum[-1] + ans[i])
            
        return prefix_sum