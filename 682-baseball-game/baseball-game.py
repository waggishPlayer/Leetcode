class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for record in operations:
            if record == "+":
                newRecord = stack[-1]+stack[-2]
                stack.append(newRecord)
            elif record == "D":
                newRecord = stack[-1]*2
                stack.append(newRecord)
            elif record == "C":
                stack.pop()
            else:
                stack.append(int(record))

        return sum(stack)