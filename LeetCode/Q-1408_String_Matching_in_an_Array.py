class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        sorted_words = sorted(words, key=lambda x: len(x))
        ans = set()
        
        
        for i, word in enumerate(sorted_words):
            for j in range(i+1, len(sorted_words)):
                if word in sorted_words[j]:
                    ans.add(word)

        return ans