class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #split the array into two arrays negative and positive

        negative_array = []
        positive_array = []
        merged_array = []

        for i in nums:
            if i < 0:
                negative_array.append(i)
            else:
                positive_array.append(i)
        
        #looping through both list at the same time and make the requirement
        for j in range(len(positive_array)):
            merged_array += [positive_array[j], negative_array[j]]
        
        return merged_array


        
