class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        pointer = 0

        while pointer < len(asteroids):
            if len(stack) > 0 and asteroids[pointer] < 0 and stack[-1] > 0:
                val = (-1) * asteroids[pointer]
                if val > stack[-1] and stack[-1]:
                    stack.pop()
                elif val < stack[-1]:
                    pointer +=1
                else:
                    stack.pop()
                    pointer +=1
            else:
                stack.append(asteroids[pointer])
                pointer += 1

        return stack