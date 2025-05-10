class MinStack:
    # Time-Complexity: O(1) for all operations
    # Space-Complexity: O(n) where n is size of stack

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.minStack) > 0):
            val = min(val, self.minStack[-1])
            self.minStack.append(val)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        