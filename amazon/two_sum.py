from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}

        for i, n in enumerate(nums):
            if n in c:
                return [c[n], i]
            else:
                c[target - n] = i
        return []

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))