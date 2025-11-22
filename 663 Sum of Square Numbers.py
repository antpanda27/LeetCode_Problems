import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0                       # Lowest Value
        b = math.ceil(math.sqrt(c)) # Highest value
        while a <= b:
            if a*a + b*b == c:
                return True
            elif a*a + b*b < c:
                a += 1
            elif a*a + b*b > c:
                b -= 1
        return False