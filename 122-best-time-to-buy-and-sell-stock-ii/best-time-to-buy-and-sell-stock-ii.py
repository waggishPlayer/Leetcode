class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit  = 0
        
        if len(prices) == 1:
            return 0
        else:
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    diff = prices[i] - prices[i-1]
                    total_profit += diff
            return total_profit
        
