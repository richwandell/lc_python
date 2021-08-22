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
            compliment = {}
            all = set()
            for n in nums:
                if target - n in compliment:
                    all.add((n, compliment[target - n]))
                else:
                    compliment[n] = n
            return list(list(x) for x in all)

        def ksum(nums, target, k):
            if len(nums) == 0:
                return []

            return_vals = []

            if k == 2:
                return list(twosum(nums, target))

            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    for set in ksum(nums[i + 1:], target - nums[i], k - 1):
                        return_vals.append([nums[i]] + set)
            return return_vals

        return ksum(nums, target, 4)


s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
print(s.fourSum([2,2,2,2,2], 8))
print(s.fourSum([-2,-1,-1,1,1,2,2], 0))