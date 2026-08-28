class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        container_vol = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right-left)* min(height[right], height[left])
            container_vol = max(container_vol, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return container_vol
