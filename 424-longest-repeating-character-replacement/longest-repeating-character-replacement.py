class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        left = 0
        substringLength = 0
        replace = 0

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            mvp = max(count.values())

            while (right-left+1) - mvp > k:
                count[s[left]] -= 1
                left += 1
            
            substringLength = max(substringLength, right - left + 1)

        return substringLength


