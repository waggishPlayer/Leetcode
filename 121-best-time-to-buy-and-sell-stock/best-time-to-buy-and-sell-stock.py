class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        cur_profit = 0
        max_profit = 0

        while right < len(prices):
            cur_profit = prices[right] - prices[left]
            if cur_profit < 0:
                left = right
            else:
                max_profit = max(max_profit, cur_profit)
            right +=1
          
        return max_profit