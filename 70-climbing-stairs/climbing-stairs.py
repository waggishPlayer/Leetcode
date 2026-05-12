class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        cache = [0]*n

        cache[0] = 1
        if n > 1:
            cache[1] = 2

        for i in range(2, n):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n-1]