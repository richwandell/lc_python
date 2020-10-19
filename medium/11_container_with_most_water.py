from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        m = -1
        while l < r:
            w = abs(l - r)
            h = min(height[l], height[r])
            a = w * h
            m = max(m, a)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return m


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
print(s.maxArea([4,3,2,1,4]))
print(s.maxArea([1,2,1]))