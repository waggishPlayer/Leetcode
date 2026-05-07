class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = {}

        for i in range(len(nums)):
            check = target - nums[i]
            if check in count:
                return [count[check], i]
            else:
                count[nums[i]] = i
    

