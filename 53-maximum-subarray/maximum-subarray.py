class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current_sum = 0
        m = nums[0]

        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum > m:
                m = current_sum
            
            if current_sum < 0:
                current_sum = 0
        
        return m