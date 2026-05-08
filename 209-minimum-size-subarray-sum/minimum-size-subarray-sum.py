class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        total = 0
        min_len = float('inf')

        while right < len(nums):
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
            
            right +=1
        
        if min_len == float('inf'):
            return 0
        else:
            return min_len
