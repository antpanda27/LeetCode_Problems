class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        for x in range (1 << n): 
            subset = []

            for i in range(n):
                if (x >> i) & 1:
                    subset.append(nums[i])
            result.append(subset)
        return result
