class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        col_no = len(matrix[0])
        left = 0
        right = (len(matrix)*col_no) - 1

        while left <= right:
            mid = (left+right)//2
            row = mid // col_no
            col = mid % col_no
            current_number = matrix[row][col]
            
            if current_number > target:
                right = mid - 1
            elif current_number < target:
                left = mid + 1
            elif current_number == target:
                return True
        
        return False