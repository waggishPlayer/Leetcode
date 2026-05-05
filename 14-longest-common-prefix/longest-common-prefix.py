class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        for column in zip(*strs):
            if len(set(column)) == 1:
                prefix += column[0]
            else:
                break
        return prefix