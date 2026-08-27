class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        profit = 0

        for right in range(len(prices)):
            diff = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
            
            if diff > profit:
                profit = diff

        return profit