import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    len_a = len(alphabet)
    finished_word = ""

    for l in s:
        if 97 <= ord(l) <= 122:
            code = ord(l) - 97
            nl = alphabet[(code + k) % len_a]
            finished_word += nl
        elif 65 <= ord(l) <= 90:
            ll = l.lower()
            code = ord(ll) - 97
            nl = alphabet[(code + k) % len_a]
            finished_word += nl.upper()
        else:
            finished_word += l
    return finished_word

if __name__ == '__main__':


    print(caesarCipher("abcdefghijklmnopqrstuvwxyz", 2))
    print(caesarCipher("middle-Outz", 2))

