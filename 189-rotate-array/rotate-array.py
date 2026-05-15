class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k%len(nums)
        nums.reverse()

        self.rev_chunk(nums, 0, k-1)
        self.rev_chunk(nums, k, len(nums)-1)


    def rev_chunk(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1