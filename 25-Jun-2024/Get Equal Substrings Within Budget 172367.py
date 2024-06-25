# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0
        total_cost = 0
        left = 0

        for right in range(len(t)):
            total_cost += abs(ord(t[right]) - ord(s[right]))

            while maxCost < total_cost:
                total_cost -= abs(ord(t[left]) - ord(s[left]))
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length