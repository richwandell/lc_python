from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        rows = []
        for n in range(0, numRows + 1):
            row = [1] * (n + 1)
            for k in range(1, n):
                a = row[k-1]
                b = (n + 1 - k) / k
                row[k] = int(a * b)
            rows.append(row)
        return rows

s = Solution()
print(s.generate(5))
print(s.generate(6))
print(s.generate(30))