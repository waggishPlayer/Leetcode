class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        nums = set(nums)

        for num in nums:
            if (num - 1) not in nums:
                cur = 1

                while (num + cur) in nums:
                    cur += 1
                
                longest = max(longest, cur)

        return longest