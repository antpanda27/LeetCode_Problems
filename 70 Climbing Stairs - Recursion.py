class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def count_step(i):
            if i <= 1:
                return 1
            if i not in memo:
                memo[i] = count_step(i-1) + count_step(i-2)
            return memo[i]
            
        return count_step(n)