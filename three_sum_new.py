from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        correct = {}
        for j in range(len(nums)):
            i, k = 0, len(nums) - 1
            while i < j < k:
                s = (nums[i], nums[j], nums[k])
                total = sum(s)
                if total == 0:
                    if s not in correct:
                        correct[s] = True
                if total < 0:
                    i += 1
                else:
                    k -= 1
        return list(correct.keys())

s = Solution()
print(s.threeSum([3,0,-2,-1,1,2]))
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
