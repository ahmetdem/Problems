class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        targetArray = []
    
        for i in range(len(nums)):
            targetArray.insert(index[i], nums[i])
        
        return targetArray