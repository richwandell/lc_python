from typing import List


class Solution:
    """
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
    """
    def searchInsert(self, nums: List[int], target: int) -> int:

        def search(nums):
            if len(nums) == 0:
                return -1
            elif len(nums) == 1:
                if target <= nums[0]:
                    return 0
                elif target > nums[0]:
                    return 1
                return -1
            elif len(nums) == 2:
                if nums[0] == target: return 0
                if nums[1] == target: return 1
                if nums[0] < target < nums[1]:
                    return 1
                elif nums[1] < target:
                    return 2
                elif nums[0] > target:
                    return 0
                return -1

            left, right = nums[0:len(nums)//2], nums[len(nums)//2:]

            found_left = search(left)
            if -1 < found_left != len(left):
                return found_left
            found_right = search(right)
            if -1 < found_right != len(right):
                return len(left) + found_right

            if found_left == len(left) and found_right == 0:
                return len(left)
            elif found_left == len(left) and found_right > 0:
                return len(left) + found_right

            if left[len(left)-1] < target < right[0]:
                return len(left)
            elif right[len(right)-1] < target:
                return len(nums)
            elif target < left[0]:
                return 0
            return -1

        out = search(nums)
        return out if out > -1 else 0

s = Solution()
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 0))
print(s.searchInsert([1], 0))
print(s.searchInsert([1], 1))
print(s.searchInsert([1], 2))
print(s.searchInsert([1, 5, 6, 7, 9, 10, 11, 12, 15], 0))
print(s.searchInsert([1, 5, 6, 7, 9, 10, 11, 12, 15], 1))
print(s.searchInsert([1, 5, 6, 7, 9, 10, 11, 12, 15], 15))
print(s.searchInsert([1, 5, 6, 7, 9, 10, 11, 12, 15], 16))
print(s.searchInsert([1, 3], 0))
print(s.searchInsert([1,3,4,5,10], 0))
print(s.searchInsert([1,3,5], 0))