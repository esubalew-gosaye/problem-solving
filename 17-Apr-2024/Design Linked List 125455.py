# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None 

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def get(self, index: int) -> int:

        if self.count > index:
            cnt = 0
            ptr = self.head 
            while cnt != index:
                print(ptr.value)
                ptr = ptr.next
                cnt += 1
            return ptr.value
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head 
        self.head = node
        self.count = self.count + 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)

        if self.count == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            cnt = 0
            while cnt < self.count - 1:
                curr = curr.next
                cnt += 1
            curr.next = node
            self.count = self.count + 1


    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        
        if self.count == index:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif self.count > index:
            cnt = 0
            ptr = self.head

            while cnt != index - 1:
                ptr = ptr.next
                cnt += 1

            forward = ptr.next
            ptr.next = node
            node.next = forward

            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.count > index:
            if index == 0:
                hd = self.head
                self.head = self.head.next 
            elif self.count - 1 == index:
                cnt = 0
                ptr = self.head

                while cnt != index - 1:
                    ptr = ptr.next
                    cnt += 1
                ptr.next = None
            else:
                cnt = 0
                ptr = self.head

                while cnt != index - 1:
                    ptr = ptr.next
                    cnt += 1
                ptr.next = ptr.next.next
            self.count -= 1
                


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)