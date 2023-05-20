class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        copy = word
    
        check1 = copy.capitalize()
        check2 = copy.upper()
        check3 = copy.lower()

        if word in [check1, check2, check3]:
            return True
        else: return False