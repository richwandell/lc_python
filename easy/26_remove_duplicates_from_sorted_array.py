from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i, j = 0, 1
        while i < len(nums):
            if nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j


s = Solution()
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

#                 i
#        j
# [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
