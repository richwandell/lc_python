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
        # height, pos
        left = [0, 0]
        right = [0, 0]
        center = False

        for i, n in enumerate(height):

            if left[1] == 0:
                left = [n, i]

            else:
                right = [n, i]

            if right[1] - left[1] > 0:
                center = True

            # fill in the gap
            if center and left[1] < right[1] and left[0] > 0 and right[0] > 0:

                left = right
                pass
        pass

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))