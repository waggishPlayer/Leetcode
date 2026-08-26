class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count = 0

        for i in range(len(details)):
            if int(details[i][11]) > 6 or int(details[i][11]) == 6 and int(details[i][12]) > 0:
                count += 1

        return count