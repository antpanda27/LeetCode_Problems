class MinStack:

    def __init__(self):
        self.s = []
        self.min = [0]

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.min) == 0 or val < self.s[self.min[-1]]:
            self.min.append(len(self.s)-1)

    def pop(self) -> None:
        if self.min[-1] == len(self.s)-1:
            self.min.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s[self.min[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()