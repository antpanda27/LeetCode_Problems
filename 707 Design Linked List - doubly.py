class Node:
    def __init__(self, val=0, nextNode = None, prevNode = None):
        self.val = val
        self.next = nextNode
        self.prev = prevNode

class MyLinkedList:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        cur = self.head
        for _ in range(index +1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val, self.head.next, self.head)
        newNode.next.prev = newNode
        self.head.next = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val, self.tail, self.tail.prev)
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
            
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        newNode = Node(val, prev.next, prev)
        prev.next.prev = newNode
        prev.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        nxt = prev.next.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)