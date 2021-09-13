import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = "".join(sorted(grid[i]))

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            if ord(grid[i-1][j]) > ord(grid[i][j]):
                return "NO"

    return "YES"

if __name__ == "__main__":
    # print(gridChallenge(['abc', 'ade', 'efg']))
    # print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
    print(gridChallenge(['abc','lmp','qrt']))
    print(gridChallenge(['mpxz','abcd','wlmf']))
    print(gridChallenge(['abc','hjk','mpq','rtv']))
    # print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
    # print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))