class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        i, ans = 0, []
        
        while i < n-2:
            n1 = nums[i]
            k = -1 * n1
            l, r = i+1, n-1

            while l < r:
                n2 = nums[l]
                n3 = nums[r]
                if n2+n3 == k:
                    ans.append([n1, n2, n3])
                    while l < r and nums[l] == n2:
                        l += 1
                elif n2+n3 > k:
                    r -= 1
                else:
                    l += 1

            while i < n-2 and nums[i] == n1:
                i += 1

        return ans