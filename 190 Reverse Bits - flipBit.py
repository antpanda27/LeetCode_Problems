class Solution:
    def reverseBits(self, n: int) -> int:
        left, right = 0, 31
        while left < right:
            l = self.getBit(n, left)
            r = self.getBit(n, right)

            if l != r:
                n = self.flipBit(n, left)
                n = self.flipBit(n, right)
            
            left += 1
            right -= 1
        return n
        
    def getBit(self, n: int, k: int) -> int:
        return (n >> k) & 1

    def flipBit(self, n: int, k: int) -> int:
        return n ^ (1 << k)