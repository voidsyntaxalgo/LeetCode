class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        i, j = 1, 1
        curr, n = nums[0], len(nums)

        while j < n:
            if nums[j] != curr:
                curr = nums[j]
                nums[i] = nums[j]
                j += 1
                i += 1
            else:
                while j < n and nums[j] == curr:
                    j += 1
        return i