class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        ss = list(s)

        if len(s) != len(t):
            return False
        for s in ss:
            if s in t:
                t.remove(s)
        
        if len(t) == 0:
            return True
        return False