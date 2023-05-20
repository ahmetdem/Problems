class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        data = {}
        _list = s.split(" ")

        for l in pattern:
            for word in _list:
                if l not in data and word not in data.values():
                    data[l] = word
                    break

        if len(_list) != len(pattern):
            return False

        for i, pat in enumerate(pattern):
            try:
                if data[pat] != _list[i]:
                    return False
            except:
                return False
        else: return True