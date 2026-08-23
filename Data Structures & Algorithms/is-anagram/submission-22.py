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

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         s_hmap = {}
#         t_hmap = {}

#         n = len(s)

#         for i in range(n):
#             s_hmap[s[i]]=0
#             t_hmap[t[i]]=0

#         for i in range(n):
#             s_hmap[s[i]]+=1
#             t_hmap[t[i]]+=1

#         for letter in s:
#             try:
#                 if s_hmap[letter] != t_hmap[letter]:
#                     return False
#             except KeyError:
#                 return False 

#         return True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         s_hmap = {}
#         t_hmap = {}

#         for i in range(len(s)):
#             s_hmap[s[i]] = 1 + s_hmap.get(s[i], 0)
#             t_hmap[t[i]] = 1 + t_hmap.get(t[i], 0)
        
#         for key in s:
#             if s_hmap[key] != t_hmap.get(key, 0): ##works because no value in the hashmap will be zero by definition
#                 return False
        
#         return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hmap = {}
        t_hmap = {}

        for i in range(len(s)):
            s_hmap[s[i]] = 1 + s_hmap.get(s[i], 0)
            t_hmap[t[i]] = 1 + t_hmap.get(t[i], 0)
        
        return s_hmap == t_hmap
