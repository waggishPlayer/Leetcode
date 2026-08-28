class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -99999
        window = 0
        left = 0

        for right in range(len(nums)):
            window += nums[right]
            if window > max_sum:
                max_sum = window

            if window < 0:
                window  = 0
                left += 1
        
        return max_sum


        