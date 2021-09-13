import math
import os
import random
import re
import sys


"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of  integers
"""

def miniMaxSum(arr):
    s, min_val, max_val = 0, sys.maxsize*2+1, 0
    for n in arr:
        s += n
        if n < min_val:
            min_val = n
        if n > max_val:
            max_val = n
    print(s - max_val, s - min_val)


    # Write your code here


if __name__ == '__main__':
    arr = list(map(int, "256741038 623958417 467905213 714532089 938071625".rstrip().split()))

    miniMaxSum(arr)