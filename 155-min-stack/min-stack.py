class MinStack(object):

    def __init__(self):
        self.numbers = []

        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.numbers) == 0 or val < self.getMin():
            self.numbers.append((val, val))
        else:
            self.numbers.append((val, self.getMin()))
            
        

    def pop(self):
        """
        :rtype: None
        """
        self.numbers.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.numbers[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.numbers[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()