class Node:
    def __init__(self, val: str = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head, self.tail = Node(homepage), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cur = self.head

    def visit(self, url: str) -> None:
        newNode = Node(url, self.tail, self.cur)
        self.tail.prev = newNode
        self.cur.next = newNode
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev != None:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next != self.tail:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)