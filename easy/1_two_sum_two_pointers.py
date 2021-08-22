from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left, right]
            elif sum < target:
                left += 1
            else:
                right -= 1


s = Solution()

print(s.twoSum([3, 2, 4], 6))