from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def perm(lst):
            if len(lst) == 0:
                return []
            elif len(lst) == 1:
                return [lst]
            all = []
            for i, n in enumerate(lst):
                x = lst[i]
                rest = lst[:i] + lst[i+1:]
                for p in perm(rest):
                    all.append([x] + p)
            return all
        return perm(nums)

s = Solution()

print(s.permute([1,2,3]))