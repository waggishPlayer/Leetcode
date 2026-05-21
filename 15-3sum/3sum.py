class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            num = nums[i]*(-1)
            while left < right:
                if nums[left] + nums[right] > num:
                    right -= 1
                elif nums[left] + nums[right] < num:
                    left += 1
                elif nums[left] + nums[right] == num:
                    result.append([nums[i], nums[left], nums[right]])
                    left +=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return result