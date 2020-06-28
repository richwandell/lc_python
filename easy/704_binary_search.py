from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = (right - left) // 2
        while True:
            if nums[mid] == target:
                return mid
            if left == right:
                return -1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = max(0, mid - 1)
            mid = left + (right - left) // 2




nums = [-1,0,3,5,9,12]
s = Solution()
print(s.search(nums, 9))
print(s.search(nums, 2))
print(s.search(nums, -1))

print(s.search([2,5], 0))