class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        list_of_string = ["" for i in range(len(s))]
        for i in s:
            list_of_string[int(i[-1])-1] = i[:-1]

        return " ".join(list_of_string)
