class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        drop = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                drop += 1
            
        if drop > 1:
            return False
        else:
            return True