from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in saved:
                return [saved[nums[i]], i]
            else:
                saved[complement] = i

s = Solution()

print(s.twoSum([3, 2, 4], 6))