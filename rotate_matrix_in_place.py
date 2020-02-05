from typing import List
import pprint


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for y in range(len(matrix)):
            for x in range(y):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]







input = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

output = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

s = Solution()

s.rotate(input)

print(pprint.pprint(input, width=15))