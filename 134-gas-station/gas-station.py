class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        currentTank = 0
        index = 0

        for i in range(len(gas)):
            currentTank += gas[i] - cost[i]

            if (gas[i] - cost[i]) > currentTank:
                index = i
            if currentTank < 0:
                index = i + 1
                currentTank = 0

        return index
            
        