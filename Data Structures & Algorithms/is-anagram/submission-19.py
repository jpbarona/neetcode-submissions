# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         t = list(t)
#         ss = list(s)

#         if len(s) != len(t):
#             return False
#         for s in ss:
#             if s in t:
#                 t.remove(s)
        
#         if len(t) == 0:
#             return True
#         return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hmap = {}
        t_hmap = {}

        n = len(s)

        for i in range(n):
            s_hmap[s[i]]=0
            t_hmap[t[i]]=0

        for i in range(n):
            s_hmap[s[i]]+=1
            t_hmap[t[i]]+=1

        for letter in s:
            try:
                if s_hmap[letter] != t_hmap[letter]:
                    return False
            except KeyError:
                return False 

        return True