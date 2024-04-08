# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        string = [ord(i) - 97 for i in s]


        ans = [0] * n
        for shift in shifts:
            add = 1 if shift[2] else -1
            ans[shift[0]] = ans[shift[0]] + add

            if shift[1] + 1 < n:
                ans[shift[1] + 1] = -1 * add + ans[shift[1] + 1]


        prefix_sum = [ans[0]]
        for i in range(1, n):
            prefix_sum.append(prefix_sum[-1] + ans[i])

        return "".join([chr(97 + (string[j] + prefix_sum[j])%26)for j in range(n)])