class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cur = 0
        s = nums[0]

        for i in range(len(nums)):
            cur += nums[i]

            if cur > s:
                s = cur

            if cur < 0:
                cur = 0
            
        return s