class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for char in tokens:
            if char == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second+first))
            elif char == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(float(second)/first))
            elif char == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second*first))
            elif char == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second-first))
           
            else:
                stack.append(int(char))

        return stack[-1]