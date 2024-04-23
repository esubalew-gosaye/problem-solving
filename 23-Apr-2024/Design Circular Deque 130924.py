# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.deque = deque()

    def insertFront(self, value: int) -> bool:
        if self.size > self.count:
            self.deque.appendleft(value)
            self.count += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size > self.count:
            self.deque.append(value)
            self.count += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if 0 < self.count:
            self.deque.popleft()
            self.count -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if 0 < self.count:
            self.deque.pop()
            self.count -= 1
            return True
        return False

    def getFront(self) -> int:
        return self.deque[0] if 0 < self.count else -1

    def getRear(self) -> int:
        return self.deque[-1] if 0 < self.count else  -1

    def isEmpty(self) -> bool:
        return 0 == self.count

    def isFull(self) -> bool:
        return self.size == self.count


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()