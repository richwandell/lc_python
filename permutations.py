from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cache = {}
        for i , n in enumerate(nums):
            if n not in cache:
                cache[n] = [n]
            else:
                cache[n].append(n)
        return cache

s = Solution()

print(s.permute([1,2,3]))