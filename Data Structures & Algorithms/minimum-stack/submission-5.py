class MinStack:
    def __init__(self):
        self._stack = []
        self.minItems = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self.minItems) == 0:
            self.minItems.append(val)
            return
        
        minItem = self.minItems[-1]
        self.minItems.append(min(minItem, val))

        if len(self._stack) != len(self.minItems):
            raise ValueError(f"len(self._stack) ({len(self._stack)}) != len(self.minItems) ({len(self.minItems)})")

    def pop(self) -> None:
        self._stack.pop()
        self.minItems.pop()

        if len(self._stack) != len(self.minItems):
            raise ValueError(f"len(self._stack) ({len(self._stack)}) != len(self.minItems) ({len(self.minItems)})")

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self.minItems[-1]
