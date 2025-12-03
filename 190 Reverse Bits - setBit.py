class Solution:
    def reverseBits(self, n: int) -> int:
        left, right = 0, 31
        while left < right:
            l = self.getBit(n, left)
            r = self.getBit(n, right)

            n = self.setBit(n, left, r)
            n= self.setBit(n, right, l)
            
            left += 1
            right -= 1
        return n
        
    def getBit(self, n: int, k: int) -> int:
        return (n >> k) & 1

    def setBit(self, n: int, k: int, val: int) -> int:
        if val == 1:
            return n | (1 << k)
        else:
            return n & ~(1 << k)