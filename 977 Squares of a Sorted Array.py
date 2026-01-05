class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        for i in range(0, len(nums)):
            nums[i] = nums[i] ** 2
            i += 1
        return sorted(nums)