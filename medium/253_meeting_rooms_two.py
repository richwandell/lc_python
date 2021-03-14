from heapq import heappush, heappop
from typing import List


class Solution:
    """
    Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum
    number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        heap = []
        num = 1
        for int in intervals:
            if len(heap) > 0:
                if not (heap[0] <= int[0]):
                    num += 1
            heappush(heap, int[1])
        return num

s = Solution()
# print(s.minMeetingRooms([[0,30],[5,10],[15,20]]))
# print(s.minMeetingRooms([[7,10],[2,4]]))
# print(s.minMeetingRooms([[13,15],[1,13]]))
print(s.minMeetingRooms([[1,5],[8,9],[8,9]]))