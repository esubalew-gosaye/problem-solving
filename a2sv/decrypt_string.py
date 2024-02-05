class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        output = ""
        
        i = len(s)
        while i > 0:
            index = i - 1
            if s[index] == "#":
                code = s[index-2:index]
                output += alphabet[int(code)-1]
                i = index - 2
            else:
                output += alphabet[int(s[index])-1]
                i = index
        return output[::-1]
