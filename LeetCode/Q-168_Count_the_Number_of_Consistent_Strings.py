class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed = set(allowed)
        res = 0
        
        for word in words:
            if allowed >= set(word):
                res += 1

        return res