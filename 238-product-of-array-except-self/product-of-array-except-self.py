class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_nums = [1]*(len(nums))
        right_nums = [1]*(len(nums))
        answer = [1]*(len(nums))

        for i in range(1, len(nums)):
            left_nums[i] = nums[i-1] * left_nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            right_nums[i] = nums[i+1] * right_nums[i+1]

        for i in range(len(nums)):
            answer[i] = left_nums[i] * right_nums[i]

        return answer