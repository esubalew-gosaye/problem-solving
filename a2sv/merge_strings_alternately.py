class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        ind = 1
        for i in word2:
            word1.insert(ind, i)
            ind += 2
        return("".join(word1))
