class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        check = set()

        for i in range(len(nums)):
            if nums[i] in check:
                return True
            else:
                check.add(nums[i])



        return False
        