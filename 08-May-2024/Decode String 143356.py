# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        closePos = {}
        st = []
        for i, c in enumerate(s):
            if c == '[':
                st.append(i)
            elif c == ']':
                closePos[st.pop()] = i

        def solve(l, r):
            num = 0
            ans = []
            while l <= r:
                c = s[l]
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == '[':
                    ans.append(num * solve(l + 1, closePos[l] - 1))
                    num = 0
                    l = closePos[l]
                else:
                    ans.append(c)
                l += 1
            return "".join(ans)

        return solve(0, len(s) - 1)