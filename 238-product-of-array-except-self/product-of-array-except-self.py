class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [0]*len(nums)
        left = 1
        right = 1

        for i in range(len(nums)):
            answer[i] = left
            left *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        
        return answer