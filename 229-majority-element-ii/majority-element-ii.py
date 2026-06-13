class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k1 = k2 = None
        v1 = v2 = 0

        for num in nums:
            if num == k1:
                v1 += 1
            elif num == k2:
                v2 += 1
            elif v1 == 0:
                k1, v1 = num, 1
            elif v2 == 0:
                k2, v2 = num, 1
            else:
                v1 -= 1
                v2 -= 1

        ans = []

        if nums.count(k1) > len(nums) // 3:
            ans.append(k1)

        if k2 != k1 and nums.count(k2) > len(nums) // 3:
            ans.append(k2)

        return ans