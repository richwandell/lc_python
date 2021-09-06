from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        def two_sum(nums, target):
            i, j = 0, len(nums)-1

            best_pair = [i, j]
            best = 0
            best_diff = 9999
            while i < j:
                s = nums[i] + nums[j]
                if s == target:
                    return [i, j], s
                elif abs(target - s) < best_diff:
                    best_diff = abs(target - s)
                    best = s
                    best_pair = [i, j]
                if s < target:
                    i += 1
                elif s > target:
                    j -= 1
            return [best_pair, best]

        def nsum(nums, n, target):
            if len(nums) < 2:
                return None, None
            if n == 2:
                return two_sum(nums, target)

            best_pair = []
            best = 9999
            for i, num in enumerate(nums):
                pair, s = nsum(nums[i+1:], n-1, target - num)
                if pair is not None:
                    if s+num == target:
                        return [i] + [x+i+1 for x in pair]
                    elif abs(s+num - target) < best:
                        best = abs(s+num - target)
                        best_pair = [i] + [x+i+1 for x in pair]
            return best_pair

        return sum(nums[x] for x in nsum(nums, 3, target))


s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))
print(s.threeSumClosest([-2,3,1,-4,5,9], 10))