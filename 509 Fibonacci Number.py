class Solution:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        if n <= 1:
            return n

        val = self.fib(n-1) + self.fib(n-2)
        self.memo[n] = val
        return val