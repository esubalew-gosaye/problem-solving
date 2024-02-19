class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1 = "eiopqrtuwy"
        row_2 = "adfghjkls"
        row_3 = "bcmnvxz"

        total_list = []
        # loop through all word and check if all of them exist in one set of row
        for word in words:
            if all(char in row_1 for char in word.lower()):
                total_list.append(word)
            elif all(char in row_2 for char in word.lower()):
                total_list.append(word)
            elif all(char in row_3 for char in word.lower()):
                total_list.append(word)
        return total_list
