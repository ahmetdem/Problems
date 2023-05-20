class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        counter = 0
        
        for word in words:
            lenght = len(word)
            isPref = s[:lenght]
            
            if word == isPref:
                counter += 1

        return counter