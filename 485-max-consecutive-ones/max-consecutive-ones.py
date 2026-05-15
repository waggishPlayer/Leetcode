class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        total = 0

        for num in nums:
            if num == 1:
                count +=1
                total = max(total, count)
            else:
                count = 0
        return total
        