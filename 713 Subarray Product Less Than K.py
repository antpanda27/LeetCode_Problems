class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count, curProd, j = 0, 1, 0
        for i in range(len(nums)):
            curProd *= nums[i]
            while curProd >= k and j <= i:
                j += 1
                curProd //= nums[j-1]
            count += i - j + 1
        return count