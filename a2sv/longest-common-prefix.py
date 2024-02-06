class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        try:
            for i in range(len(strs[0])):
                pre = strs[0][i]
                if all(pre == word[i] for word in strs):
                    prefix += pre 
                else:
                    return prefix
        except IndexError:
            return prefix
        return prefix

       
