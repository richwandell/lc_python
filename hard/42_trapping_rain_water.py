from typing import List


class Solution:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.

    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9
    """
    def trap(self, height: List[int]) -> int:

        total = 0
        for i, n in enumerate(height):
            left_max = 0
            right_max = 0

            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])

            for j in range(i, len(height)):
                right_max = max(right_max, height[j])

            m = min(left_max, right_max)
            if m > n:
                total += m - n

        return total

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))