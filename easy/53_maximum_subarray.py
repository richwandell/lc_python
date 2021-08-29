from typing import List


class Solution:
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Kadane's algorithm
    """
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        best, current = nums[0], nums[0]
        for num in nums[1:]:
            current = max(num, current+num)
            best = max(best, current)
        return best

s = Solution()
print(s.maxSubArray([-2,-1]))
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5,4,-1,7,8]))