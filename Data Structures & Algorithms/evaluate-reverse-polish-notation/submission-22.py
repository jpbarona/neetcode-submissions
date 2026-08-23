class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                x = int(token)
                stack.append(x)
            except ValueError:
                if len(stack) < 2:
                    raise ValueError("wrong")
                print(stack)
                x = False
                b = stack.pop()
                a = stack.pop() 
                print(f"{token!r}") 
                match token:
                    case "+":
                        x = a + b
                        print(f"{x} = {a} + {b}")
                    case "*":
                        x = a * b
                        print(f"{x} = {a} * {b}")
                    case "-":
                        x = a - b
                        print(f"{x} = {a} - {b}")
                    case "/":
                        x = int(a/b)
                        print(f"{x} = {a} // {b}")
                stack.append(x)
        
        return stack[-1]
