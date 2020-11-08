from typing import List


class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        c = {}
        for i, num in enumerate(numbers):

            l = target - num
            if l in c:
                return [c[l] + 1, i + 1]

            c[num] = i


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0, len(numbers) - 1

        while i < j:

            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]


s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,3,4], 6))
print(s.twoSum([-1,0], -1))
print(s.twoSum([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997], 542))

# i           j
# 1, 2, 3, 4, 5 8
