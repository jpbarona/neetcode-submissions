class Solution:
    SEPARATOR = "<<|<<|>>|>>"
    def encode(self, strs: List[str]) -> str:
        out = ""
        for x in strs:
            out += x
            out += self.SEPARATOR

        return out

    def decode(self, s: str) -> List[str]:
        return s.split(self.SEPARATOR)[:-1]