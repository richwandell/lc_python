from typing import List


class Solution:
    """
    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def twosum(nums, target):
            res = []
            left, right = 0, len(nums) - 1
            while left < right:
                current = nums[left] + nums[right]
                if current < target or (left > 0 and nums[left] == nums[left - 1]):
                    left += 1
                elif current > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
            return res

        def ksum(nums, target, k):
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res

            if k == 2:
                return twosum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in ksum(nums[i+1:], target - nums[i], k-1):
                        res.append([nums[i]] + subset)

            return res

        nums = sorted(nums)

        return ksum(nums, target, 4)

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
print(s.fourSum([2,2,2,2,2], 8))
print(s.fourSum([-2,-1,-1,1,1,2,2], 0))
