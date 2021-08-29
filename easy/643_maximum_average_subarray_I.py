from typing import List


class Solution:
    """
    You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, k - 1

        c = sum(nums[i:j])
        m = None
        while j < len(nums):
            c += nums[j]
            a = c / k
            if m is None or a > m:
                m = a
            c -= nums[i]
            i += 1
            j += 1
        return m

s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
print(s.findMaxAverage([5], 1))
print(s.findMaxAverage([-1], 1))