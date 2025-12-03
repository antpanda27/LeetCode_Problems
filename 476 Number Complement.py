class Solution:
    def findComplement(self, num: int) -> int:
        k = 0
        length = len(bin(num)) - 3
        while k <= length:
            num ^= (1 << k)
            k += 1
        return num