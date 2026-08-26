class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        cur_max = -1

        for i in range(len(arr) -1,-1,-1):
            og_value = arr[i]
            arr[i] = cur_max

            if og_value > cur_max:
                cur_max = og_value
        
        return arr
