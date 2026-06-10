class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        curr = nums[0]
        freq = 1

        for i in range(1, n):
            if nums[i] == curr:
                freq += 1
            else:
                if freq == 1:
                    curr = nums[i]
                else:
                    freq -= 1
                
        return curr