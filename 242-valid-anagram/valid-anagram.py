class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = {}
        check = {}
        if len(s) != len(t):
            return False

        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        for char in t:
            if char not in check:
                check[char] = 1
            else:
                check[char] += 1

        if check == count:
            return True
        else:
            return False