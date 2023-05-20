from collections import Counter
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        common = Counter(words[0])
        for s in words[1:]:
            common &= Counter(s)
        return list(common.elements())







