class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        minVal = float('inf')

        for num in nums:
            sums = 0
            
            while num > 0:
                sums += num % 10
                num = num // 10
            
            if sums < minVal:
                minVal = sums
        
        return minVal