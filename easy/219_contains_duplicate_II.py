from typing import List


class Solution:
    """
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: return False
        set = {}
        for i, item in enumerate(nums):
            if item in set:
                return True
            set[item] = item
            if len(set) > k:
                del set[nums[i - k]]
        return False


s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3))
print(s.containsNearbyDuplicate([1,0,1,1], 1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(s.containsNearbyDuplicate([1,2,1], 0))
print(s.containsNearbyDuplicate([4,1,2,3,1,5], 3))
print(s.containsNearbyDuplicate([0,1,2,3,2,5], 3))
print(s.containsNearbyDuplicate([1,2,2,3], 3))
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))