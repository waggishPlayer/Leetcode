class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cache = [amount+1]*(amount+1)
        cache[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    cache[i] = min(cache[i], cache[i-coin] + 1)

        if cache[amount] == amount + 1:
            return -1
        else: 
            return cache[amount]



