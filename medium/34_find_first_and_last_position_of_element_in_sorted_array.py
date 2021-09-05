from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        def search_first(start, end):
            if end - start == 1:
                if nums[start] == target:
                    return start
                elif nums[end] == target:
                    return end
                return -1

            mid = (start + end) // 2
            if nums[mid] == target and (mid > 1 and nums[mid-1] != target):
                return mid
            elif nums[mid] >= target:
                return search_first(start, mid)
            else:
                return search_first(mid, end)

        def search_last(start, end):
            if end - start == 1:
                if nums[end] == target:
                    return end
                elif nums[start] == target:
                    return start
                return -1

            mid = (start + end) // 2
            if nums[mid] == target and (mid < len(nums) and nums[mid+1] != target):
                return mid
            elif nums[mid] > target:
                return search_last(start, mid)
            else:
                return search_last(mid, end)

        found_start = search_first(0, len(nums)-1)
        found_end = search_last(0, len(nums)-1)
        return [found_start, found_end]

s = Solution()

print(s.searchRange([5,7,7,7,7,7,8,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
print(s.searchRange([], 6))
print(s.searchRange([2, 2], 6))
print(s.searchRange([2, 2], 2))
print(s.searchRange([1, 2, 3], 3))