class MinStack:

    def __init__(self):
        self.stack = []
        self.t = 0
        self.minumum = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.minumum = val
        elif val < self.minumum:
            self.minumum = val
        self.t = val
        self.stack.append(val)

    def pop(self) -> None:
        new = []
        new_min = self.stack[0]
        for i in range(len(self.stack) - 1):
            if self.stack[i] < new_min:
                new_min= self.stack[i]
            new.append(self.stack[i])
        self.stack = new
        self.minumum = new_min
        if self.stack:
            self.t = self.stack[-1]

    def top(self) -> int:
        return self.t

    def getMin(self) -> int:
        return self.minumum