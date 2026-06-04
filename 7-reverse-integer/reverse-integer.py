class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev_x = 0

        while x > 0:
            num = x % 10
            rev_x = rev_x * 10 + num
            x = x // 10

        if rev_x < -(2**31) or rev_x > 2**31 - 1:
            return 0

        return rev_x * sign
        