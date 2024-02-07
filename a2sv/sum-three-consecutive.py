class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        middle_num_int = num // 3
        middle_num_float = num / 3
        
        if(middle_num_int == middle_num_float):
            return [middle_num_int - 1, middle_num_int, middle_num_int + 1]
        else:
            return []
