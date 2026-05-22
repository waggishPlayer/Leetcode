class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        cur_sub = 0
        longest_sub = 0
        window = set()

        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                right +=1
            else:
                window.remove(s[left])
                left +=1

            cur_sub = right - left
            longest_sub = max(longest_sub, cur_sub)

        return longest_sub  