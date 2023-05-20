class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """

        strings = "abc"

        if len(s) == 1:
            return "a"

        for i, l in enumerate(s):
            
            letter = ""
            if l == "?":
                if i == 0:
                    letter = s[1]
                elif i == (len(s) - 1):
                    letter = s[-2]
                else:
                    letter = (s[i+1], s[i-1])
            else: continue

            for string in strings:
                if string not in letter:
                    s = s[:i] + string + s[i+1:]
                    break
        
        return s