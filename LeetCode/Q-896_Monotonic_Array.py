class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        copy = nums.copy()
        copy.sort()
        
        if nums == copy or nums == list(reversed(copy)):
            return True
        else: return False
    