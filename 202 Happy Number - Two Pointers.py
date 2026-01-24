class Solution:
    def isHappy(self, n: int) -> bool:

        def nextNum(num: int) -> int:
            return sum([int(x)**2 for x in str(num)])

        m = n
        while m != 1:
            n = nextNum(n)
            m = nextNum(nextNum(m))
            if n == m:
                return n == 1
        return True