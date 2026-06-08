class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        curr_sum, size, curr = 0, float("inf"), 0

        while r < n:
            if curr_sum >= k:
                size = min(size, curr)
                curr_sum -= nums[l]
                l += 1
                curr -= 1
            else:
                curr_sum += nums[r]
                r += 1
                curr += 1

        while curr_sum >= k:
            size = min(size, curr)
            curr_sum -= nums[l]
            l += 1
            curr -= 1

        return 0 if size == float("inf") else size