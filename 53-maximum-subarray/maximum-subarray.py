class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = max(nums)
        
        if s < 0:
            return s

        curr = 0
        s = 0

        for num in nums:
            curr = max(curr + num, 0)
            s = max(s, curr)

        return s