from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = {}
        for i in range(len(nums)):
            j, k = 0, len(nums) - 1
            while j < i < k:
                vals = (nums[j], nums[i], nums[k])
                s = sum(vals)
                if s == 0:
                    solutions[vals] = True
                if s < 0:
                    j += 1
                else:
                    k -= 1
        return solutions.keys()


s = Solution()

print(s.threeSum([-1, 0, 1, 2, -1, -4]))