import math
import os
import random
import re
import sys

def palindromeIndex(s):
    l, r = 0, len(s) - 1

    remove = []
    while l < r:
        lc = s[l]
        rc = s[r]

        if lc == rc:
            l += 1
            r -= 1
        elif l+1 < r and s[l+1] == rc:
            remove.append(l)
            l += 1
        elif r - 1 > l and s[r-1] == lc:
            remove.append(r)
            r -= 1
    if len(remove) == 1:
        return remove[0]
    return -1





if __name__ == '__main__':


    print(palindromeIndex("aaab"))
    print(palindromeIndex("baa"))
    print(palindromeIndex("aaa"))
    print(palindromeIndex(""))

