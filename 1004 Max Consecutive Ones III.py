class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = 0
        zeroCount = 0
        currCount = 0
        maxCount = 0
        for i in nums:
            if i == 0:
                zeroCount += 1
            currCount += 1
            while zeroCount > k:
                if nums[j] == 0:
                    zeroCount -= 1
                j += 1
                currCount -= 1
            maxCount = max(maxCount, currCount)
        return maxCount