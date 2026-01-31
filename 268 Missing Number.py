class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        
        for x in nums:
            ans ^= x
        
        for i in range(len(nums)+1):
            ans ^= i

        return ans