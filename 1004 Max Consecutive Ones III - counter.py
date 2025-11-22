class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = Counter()
        j = 0
        maxCount = 0
        for i in range(len(nums)):
            count[nums[i]] += 1
            while count[0] > k:
                count[nums[j]] -= 1
                j += 1
            maxCount = max(maxCount, sum(count.values()))
        return maxCount
