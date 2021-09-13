import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    total_swaps = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] == i + 1:
            continue
        if i - 1 >= 0 and q[i - 1] == i + 1:
            total_swaps += 1
            q[i - 1], q[i] = q[i], q[i - 1]
        elif i - 2 >= 0 and q[i - 2] == i + 1:
            total_swaps += 2
            q[i - 2], q[i - 1], q[i] = q[i - 1], q[i], q[i - 2]
        else:
            print("Too chaotic")
            return
    print(total_swaps)

if __name__ == "__main__":
    minimumBribes([2, 1, 5, 3, 4])
    minimumBribes([2, 5, 1, 3, 4])
    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])