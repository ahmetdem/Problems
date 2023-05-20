class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        right = -10e5

        for i in range(len(nums)-k+1):
            left = sum(nums[i:i+k])/k

            if left > right:
                right = left

        return right