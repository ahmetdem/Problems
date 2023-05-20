class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        curr_sum = 0
        
        for n in nums:
            curr_sum = max(curr_sum + n, n)
            max_sum = max(max_sum, curr_sum) 
            
        return max_sum
    