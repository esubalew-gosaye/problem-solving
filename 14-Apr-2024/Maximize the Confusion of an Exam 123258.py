# Problem: Maximize the Confusion of an Exam - https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n=len(answerKey)
        def maxW(c):
            ans=0
            flip=0
            l=0
            for r in range(n):
                if answerKey[r]!=c: 
                    flip+=1
                if flip>k: 
                    while answerKey[l]==c: 
                        l+=1
                    l+=1  
                    flip-=1  
                ans=max(ans, r-l+1)  
            return ans
        
        return max(maxW('T'), maxW('F'))