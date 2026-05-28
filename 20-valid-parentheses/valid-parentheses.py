class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            else:
                if bracket == ")":
                    if len(stack) > 0 and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                if bracket == "}":
                    if len(stack) > 0 and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                if bracket == "]":
                    if len(stack) > 0 and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
        
        if len(stack) == 0:
            return True
        else:
            return False