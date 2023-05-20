class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []
        
        for i in range(len(words)):
            word = words[i].lower()
            for row in rows:
                if set(row) >= set(word):
                    ans.append(words[i])
        else:
            return ans
