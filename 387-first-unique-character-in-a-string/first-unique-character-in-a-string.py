class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        check = {}

        for i in range(len(s)):
            if s[i] in check:
                check[s[i]] += 1
            else:
                check[s[i]] = 1
        
        for i in range(len(s)):
            if check[s[i]] == 1:
                return i
        
        return -1