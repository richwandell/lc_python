import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):

    bricks = [1, 2, 3, 4]

    def make_rows(bricks, so_far):
        sfs = sum(so_far)
        if sfs == m:
            n = []
            for item in so_far:
                if len(n) > 0:
                    v = item + n[-1]
                    n.append(v)
                else:
                    n.append(item)
            return [n]
        elif sfs > m:
            return []

        results = []
        for brick in bricks:
            so_far.append(brick)
            rows = make_rows(bricks, so_far)
            results += rows
            so_far.pop()
        return results

    def make_layouts(brick_rows, so_far, v_lines):
        if len(so_far) == n:
            return [so_far[:]]
        elif len(so_far) > n:
            return []

        results = []
        for i in range(len(brick_rows)):
            so_far.append(i)
            hit_n = False
            for num in brick_rows[i]:
                if num != m:
                    if num not in v_lines:
                        v_lines[num] = 0
                    v_lines[num] += 1
                    if v_lines[num] == n:
                        hit_n = True
                        break
            if not hit_n:
                l = make_layouts(brick_rows, so_far, v_lines)
                results += l
            so_far.pop()
        return results

    rows = sorted(make_rows(bricks, []), key=lambda x: len(x), reverse=True)

    layouts = make_layouts(rows, [], {})

    return len(layouts)



if __name__ == '__main__':


    print(legoBlocks(2, 2))
    print(legoBlocks(3, 2))
    print(legoBlocks(4, 5))
    # print(legoBlocks(7, 4))