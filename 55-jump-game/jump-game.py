class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        goal = len(nums) - 1

        for i in range(len(nums)):
            index = len(nums) - i - 1
            if (index + nums[index]) >= goal:
                goal = index

        if goal == 0:
            return True
        else:
            return False