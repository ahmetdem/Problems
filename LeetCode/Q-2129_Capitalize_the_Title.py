class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """

        res = []

        for word in title.split(" "):

            if len(word) <= 2:
                word = word.lower()
            else: 
                word = word.capitalize()

            res.append(word)

        return " ".join(res)