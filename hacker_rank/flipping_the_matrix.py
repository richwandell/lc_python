import math
import os
import random
import re
import sys

"""

"""

def flippingMatrix(matrix):
    n = len(matrix) // 2

    out = 0
    for i in range(n):
        for j in range(n):
            l = []
            l.append(matrix[i][j])  # current matrix
            l.append(matrix[2 * n - 1 - i][j])  # bottom left
            l.append(matrix[i][2 * n - 1 - j])  # top right
            l.append(matrix[2 * n - 1 - i][2 * n - 1 - j])  # bottom right
            out += max(l)
    return out

if __name__ == '__main__':
    # matrix = [[1, 2], [3, 4]]
    matrix = [
        [112, 42, 83, 119],
        [56, 125, 56, 49],
        [15, 78, 101, 43],
        [62, 98, 114, 108]
    ]

    out = flippingMatrix(matrix)

    print(out)