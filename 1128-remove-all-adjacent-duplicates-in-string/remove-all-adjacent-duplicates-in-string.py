class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if len(stack) > 0 and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)