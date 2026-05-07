class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        left, right = 0,1

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right

            profit = max(profit, prices[right] - prices[left])
            right +=1
        
        return profit
