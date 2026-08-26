class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left = 0
        ones = 0
        n = len(s)
        ans = ""


        for right in range(n):

            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left +=1 

            if ones == k:
                while left < right and s[left] == '0':
                    left += 1

                cur = s[left:right+1]

                if ans == "" or len(ans) > len(cur) or len(cur) == len(ans) and cur < ans:
                    ans = cur

        return ans

            

        