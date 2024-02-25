class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        count_of_one = nums.count(1)
        count_of_zero = 0
        max_sum = 0
        max_sum_list = [0]

        for i in range(len(nums)):
            if count_of_one + count_of_zero > max_sum:
                max_sum = count_of_one + count_of_zero
                max_sum_list = [i]
            elif count_of_one + count_of_zero == max_sum:
                max_sum_list += [i]

            if nums[i] == 0:
                count_of_zero += 1
            else:
                count_of_one -= 1

        if count_of_one + count_of_zero > max_sum:
            max_sum = count_of_one + count_of_zero
            max_sum_list = [i+1]
        elif count_of_one + count_of_zero == max_sum:
            max_sum_list += [i+1]


        return max_sum_list

        
