class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if (j - i + 1) % 2 == 1:
                    ans += sum(arr[i:j+1])
        return ans