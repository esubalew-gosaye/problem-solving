# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_index = [0]
        self.count = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.stack[self.min_index[-1]]:
            self.min_index.append(self.count)
        self.count += 1
        

    def pop(self) -> None:
        self.count -= 1
        if self.min_index[-1] == self.count:
            if len(self.min_index) > 1:
                self.min_index.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_index[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()