class Solution:
    def reverse(self, x: int) -> int:
        ltz = False
        t = x
        if x < 0:
            ltz = True
            t = -x
        n = 0
        while t > 0:
            t1 = t % 10
            n = (n * 10) + t1
            t = t // 10
            if n > 2147483647:
                return 0
        return -n if ltz else n


s = Solution()
out1 = s.reverse(123)
out2 = s.reverse(-123)
out3 = s.reverse(1534236469)
print(out1, out2, out3)