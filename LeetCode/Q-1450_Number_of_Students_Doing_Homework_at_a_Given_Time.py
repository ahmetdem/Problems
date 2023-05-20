class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """

        result = 0

        for i in range(len(startTime)):
        
                if queryTime in range(startTime[i], endTime[i]+1):
                    result += 1
                else:
                    if startTime[i] == queryTime:
                        result += 1

        else: return result