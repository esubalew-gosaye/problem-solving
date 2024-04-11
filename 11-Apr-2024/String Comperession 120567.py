# Problem: String Comperession - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []

        char = ""
        count = 0
        len_nw = 0
        first = 0
        for i in chars:
            if i == char:
                count += 1
            else:
                if char != "" and count == 0:
                    chars[first] = char
                    first += 1
                elif char != "":
                    for j in (char + str(count + 1)):
                        chars[first] = j
                        first += 1
                char = i
                print(char)
                count = 0
        else:
            if count != 0:
                for j in (char + str(count + 1)):
                    chars[first] = j
                    first += 1
            else:
                chars[first] = char
                first += 1
        print(first)
        return first
            