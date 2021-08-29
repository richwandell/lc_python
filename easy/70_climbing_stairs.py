class Solution:
    def climbStairs(self, n: int) -> int:
        so_far_results = {}

        def climb(so_far):
            if so_far in so_far_results:
                return so_far_results[so_far]
            if so_far > n:
                return 0
            elif so_far == n:
                return 1

            one = climb(so_far+1)
            so_far_results[so_far+1] = one
            two = climb(so_far+2)
            so_far_results[so_far + 2] = two
            return one + two

        return climb(0)

s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(35))