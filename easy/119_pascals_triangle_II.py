from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        row = [1]*(rowIndex+1)
        for k in range(1, rowIndex):
            a = row[k - 1]
            b = (rowIndex + 1 - k) / k
            row[k] = round(a * b)
        return row

s = Solution()
print(s.getRow(11))
# print(s.getRow(3))
# print(s.getRow(0))
# print(s.getRow(1))
# print(s.getRow(5))
# print(s.getRow(6))
# print(s.generate(30))