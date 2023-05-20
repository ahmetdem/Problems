class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """

        lenght = len(pref)
        counter = 0
        
        for word in words:
            isPref = word[:lenght]
            
            if isPref == pref:
                counter += 1
                
        return counter