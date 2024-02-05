class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(s)):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]
        else:
            return sorted_t[-1]
