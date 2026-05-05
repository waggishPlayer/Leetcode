class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = min(len(word) for word in strs)
        prefix = ""

        for i in range(min_len):
            check = strs[0][i]

            for word in strs:
                if check != word[i]:
                    return prefix
            
            prefix += strs[0][i]
        return prefix