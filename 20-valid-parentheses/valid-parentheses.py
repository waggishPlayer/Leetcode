class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictionary = {")":"(", "}":"{", "]":"["}
        stack = []

        for char in s:
            if char in dictionary:
                if stack and stack[-1] == dictionary[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0