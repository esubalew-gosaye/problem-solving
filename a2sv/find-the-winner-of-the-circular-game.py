class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        new_list = [i for i in range(1, n + 1)]
        
        ind = 0
        while n != 1:
            index = (ind + k - 1) % n
            popd = new_list.pop(index)
            ind = index
            n -= 1
            
        return new_list[0]
