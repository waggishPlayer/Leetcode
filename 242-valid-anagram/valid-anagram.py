class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        for char in t:
            if char not in count:
                return False
            
            count[char] -= 1
            if count[char] < 0:
                return False

        return True