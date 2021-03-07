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
        if len(height) == 0:
            return 0
        left_max = [0]*len(height)
        right_max = [0]*len(height)
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i - 1])
        right_max[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        total = 0
        for i, n in enumerate(height):
            m = min(left_max[i], right_max[i])
            if m > n:
                total += m - n

        return total

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))