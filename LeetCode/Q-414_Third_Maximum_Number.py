class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        _set = set(nums)
        nums2 = list(_set)

        if len(nums2) < 3:
            return max(nums2)

        return sorted(nums2)[-3]