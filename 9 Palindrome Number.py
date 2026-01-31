class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        ans = 0
        digit = 0
        y = x

        if x < 0 or x % 10 == 0:
            return False
        while y:
            digit = y % 10
            ans = (ans * 10) + digit
            y = y // 10
        return ans == x