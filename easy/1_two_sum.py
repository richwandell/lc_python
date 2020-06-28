from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = {}
        for i, n in enumerate(nums):
            complement = target - n
            if n in saved:
                return [saved[n], i]
            else:
                saved[complement] = i

s = Solution()

print(s.twoSum([3, 2, 4], 6))