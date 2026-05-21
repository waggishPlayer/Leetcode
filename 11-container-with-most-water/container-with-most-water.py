class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        cur_area = 0
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            cur_area = h*(right-left)
            max_area = max(max_area, cur_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
        return max_area

        