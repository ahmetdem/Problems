class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

            
        num1, num2 = min(nums), max(nums)
        res = 0
        
        for i in range(1, num1+1):
            if num1 % i == 0 and num2 % i == 0:
                if i > res:
                    res = i       
                        
        return res