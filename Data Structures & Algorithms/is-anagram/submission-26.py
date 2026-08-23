class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        EMPTY = ""
        if len(s) != len(t):
            return False
        
        for char_s in s:
            if t not in t:
                return False
            t = t.replace(char_s, EMPTY, 1)

        result = t == ""
        return result