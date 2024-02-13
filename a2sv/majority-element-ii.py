class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_num = set() # define a set of majority to avoid replica
        list_frequency = Counter(nums) # find the frequency of each number

        for i in nums:
            if list_frequency[i] > int(len(nums)/3):
                majority_num.add(i)

        return majority_num
