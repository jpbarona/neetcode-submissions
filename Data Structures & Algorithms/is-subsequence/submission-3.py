class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        i = 0

        while i < len(s):
            char = s[i]
            found = False

            while not found:
                if ptr >= len(t):
                    return False

                if char == t[ptr]:
                    i += 1
                    found = True

                ptr += 1

        return True