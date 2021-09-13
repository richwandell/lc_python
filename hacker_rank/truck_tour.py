import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    sys.setrecursionlimit(1500)
    made_it = None

    def try_path(pumps, gas_left, so_far, start_pump):
        nonlocal made_it
        if len(so_far) == len(petrolpumps):
            made_it = start_pump
            return

        for i in range(len(pumps)):
            t_range, distance = pumps[i][0], pumps[i][1]
            if t_range + gas_left >= distance:
                so_far.append(pumps[i])
                try_path(pumps[0:i] + pumps[i+1:], t_range+gas_left-distance, so_far, start_pump)
                so_far.pop()
                if made_it is not None:
                    return


    for i in range(len(petrolpumps)):
        t_range, distance = petrolpumps[i][0], petrolpumps[i][1]
        if t_range >= distance:
            try_path(petrolpumps[0:i] + petrolpumps[i+1:], t_range - distance, [petrolpumps[i]], i)
        if made_it is not None:
            break

    return made_it


if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    print(truckTour([[1, 5], [10, 3], [3, 4]]))