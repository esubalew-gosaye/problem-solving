# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def check_substring(self, cs, ct):
        for char in ct:
            if not (char in cs and cs[char] >= ct[char]): 
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        counter_s = {}

        n = len(s)
        m = len(t)

        left = start = 0
        min_len = float('inf')

        if m > n or n == "" or m == "":
            return ""

        for right in range(n):
            
            counter_s[s[right]] = counter_s.get(s[right], 0) + 1

            while self.check_substring(counter_s, counter):
                

                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    start = left
                if counter_s.get(s[left]) == 0:
                    counter_s.pop(s[left])
                else:
                     counter_s[(s[left])] -= 1
                   

                left += 1
        # print("min-len", min_len)

        # return 0 if min_len == float('-inf') else min_len
        return "" if min_len == float('inf') else s[start: start + min_len]