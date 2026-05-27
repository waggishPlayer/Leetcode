class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lower = {}
        upper = {}
        count = 0

        for i, char in enumerate(word):
            if char.islower():
                lower[char] = i
            elif char.isupper():
                if char not in upper:
                    upper[char] = i

        for char, index in lower.items():
            if char.upper() in upper and upper[char.upper()] > lower[char]:
                count += 1
            
        return count