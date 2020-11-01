from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j, = 0, 0

        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


s = Solution()
a = [3,2,2,3]
assert s.removeElement(a, 3) == 2 and a[0] == 2 and a[1] == 2
a = [0,1,2,2,3,0,4,2]
assert s.removeElement(a, 2) == 5 and a[0] == 0 and a[1] == 1 and a[2] == 3 and a[3] == 0 and a[4] == 4

#      j
#      i
# [0,1,2,2,3,0,4,2]
#      i   j
# [0,1,2,2,3,0,4,2]