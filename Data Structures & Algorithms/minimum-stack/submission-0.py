class MinStack:
    def __init__(self):
        self._stack = []
        self.minItem = math.inf

    def push(self, val: int) -> None:
        self._stack.append(val)
        self.minItem = min(self.minItem, val)

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return min(self._stack)
