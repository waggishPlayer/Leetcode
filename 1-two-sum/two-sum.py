class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check = {}
        
        for i in range(len(nums)):
            operand = target - nums[i]
            if (target - nums[i]) in check:
                return [check[operand], i]
            else:
                check[nums[i]] = i
