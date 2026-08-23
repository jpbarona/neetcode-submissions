class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ("(", "[", "{"):
                match char:
                    case "(":
                        stack.append(")")
                    case "[":
                        stack.append("]")
                    case "{":
                        stack.append("}")
                continue
            if len(stack)==0:
                return False
            expected = stack.pop()
            if char != expected:
                return False

        return (len(stack) == 0)