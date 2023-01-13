class Solution:
   
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(n+1):
            if i%3==0 and i%5==0:l+=['FizzBuzz']
            elif i%3==0: l+=['Fizz']
            elif i%2==0: l+=['Buzz']
            else: l+=[i]
        return l
