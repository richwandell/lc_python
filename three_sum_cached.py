from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSum(nums: List[int], target: int) -> List[int]:
            saved = {}
            for i, n in enumerate(nums):
                complement = target - n
                if n in saved:
                    return [saved[n], i]
                else:
                    saved[complement] = i
            return []

        saved = {}
        all = []
        for i, n in enumerate(nums):

            if n in saved:
                continue
            else:
                subset = nums[:i] + nums[i+1:]
                index = twoSum(subset, -n)
                if len(index) > 0:
                    tup = (n, subset[index[0]], subset[index[1]])
                    for t in tup:
                        saved[t] = True
                    all.append(tup)
        return all





s = Solution()
print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
print(s.threeSum([3,0,-2,-1,1,2]))
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
