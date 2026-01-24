class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for k in range(32):
            total = 0
            for n in nums:
                total += (n >> k) & 1
            if total % 3 != 0:
                ans |= (1 << k)
        if ans >= (1 << 31):
            ans -= (1 << 32)
        return ans