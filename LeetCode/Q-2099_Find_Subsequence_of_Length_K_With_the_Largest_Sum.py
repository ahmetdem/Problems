class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        val_and_index = sorted([(num, i) for i, num in enumerate(nums)])
        return [num for num, i in sorted(val_and_index[-k :], key=lambda x: x[1])]