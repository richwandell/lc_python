from collections import deque
from typing import List


class Solution:
    """
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return
    an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals

        intervals = sorted(intervals, key=lambda x: x[0])
        ri = []
        r1 = intervals[0]
        for r2 in intervals[1:]:
            if r1 == r2: continue
            if r1[0] <= r2[0] and r1[1] >= r2[0]:
                r1 = [r1[0], max(r1[1], r2[1])]
            else:
                ri.append(r1)
                r1 = r2
        ri.append(r1)

        return ri

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))
print(s.merge([[1,4],[1,4]]))
print(s.merge([[1,4],[1,5]]))