class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        result = []

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        bucket = [[] for i in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result
