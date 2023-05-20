class Solution:
    def firstUniqChar(self, s: str) -> int:

        for l in s:
            if s.count(l) == 1:
                return s.index(l)
        return -1