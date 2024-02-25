class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        num_list = []
        zero_list = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                if nums[i] == 0:
                    zero_list.append(0)
                else:
                    num_list.append(2 * nums[i])
                nums[i + 1] = 0
            else:
                if nums[i] == 0:
                    zero_list.append(0)
                else:
                    num_list.append(nums[i])

        if nums[len(nums) - 1] == 0:
            zero_list.append(0)
        else:
            num_list.append(nums[i+1])
        return num_list + zero_list
