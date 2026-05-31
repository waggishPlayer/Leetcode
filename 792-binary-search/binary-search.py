class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left <= right:
            avg = (right+left)//2
            if nums[avg] > target:
                right = avg - 1
            if nums[avg] < target:
                left = avg + 1
            if nums[avg] == target:
                return avg
            
        return -1