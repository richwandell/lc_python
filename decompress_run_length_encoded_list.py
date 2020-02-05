from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        li = []
        i = 0
        while i < len(nums):
            rlen = nums[i]
            i += 1
            j = 0
            while j < rlen:
                li.append(nums[i])
                j += 1
            i += 1

        return li


s = Solution()
print(s.decompressRLElist([1,2,3,4]))