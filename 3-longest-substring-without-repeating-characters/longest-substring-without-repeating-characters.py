class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 1:
            return 1

        right = 0
        left = 0
        max_num = 0
        window = set()

        while right < len(s):
            if s[right] in window:
                window.remove(s[left])
                left += 1

            else:
                window.add(s[right])
                right += 1
                
            max_num = max(max_num, right - left)
        
        return max_num
        