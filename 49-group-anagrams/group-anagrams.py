class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        store = {}

        for word in strs:
            sort = "".join(sorted(word))
            if sort not in store:
                store[sort] = []
  
            store[sort].append(word)

        return store.values()
