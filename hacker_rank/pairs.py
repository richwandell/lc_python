import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    cache = {}
    found = []
    for item in arr:
        if item + k in cache:
            found.append((item, item + k))
        if item - k in cache:
            found.append((item, item - k))
        cache[item] = item
    return len(found)

if __name__ == "__main__":
    # print(pairs(1, [1, 2, 3, 4]))
    print(pairs(2, [1, 5, 3, 4, 2]))