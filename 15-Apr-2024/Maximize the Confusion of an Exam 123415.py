# Problem: Maximize the Confusion of an Exam - https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        kf = k
        kt = k

        consT = it = jf = consF = 0
        max_len = 0 

        for i in range(n):
            if answerKey[i] == 'T':
                if kf == 0:
                    max_len = max(max_len, i - jf)

                    while True:
                        if answerKey[jf] == 'T':
                            jf += 1
                            kf += 1 
                            break
                        jf += 1

                kf -= 1
            else:
                if kt == 0:
                    max_len = max(max_len, i - it)

                    while True:
                        if answerKey[it] == 'F':
                            it += 1
                            kt += 1 
                            break
                        it += 1
                kt -= 1

        max_len = max(max_len, n - it)
        max_len = max(max_len, n - jf)

        return max_len