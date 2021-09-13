import math
import os
import random
import re
import sys

"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input

07:05:45PM
Sample Output

19:05:45
"""

def timeConversion(s):
    m = re.match(r'(\d{2}):(\d{2}):(\d{2})(\w+)', s)
    if m:
        hh, mm, ss, am_pm = m.groups()
        if am_pm == 'AM' and hh == '12':
            hh = '00'
        elif am_pm == 'PM':
            if int(hh) > 12:
                hh = str(int(hh) - 12)
            elif int(hh) != 12:
                hh = str(12 + int(hh))
        return f"{hh}:{mm}:{ss}"

if __name__ == '__main__':


    print(timeConversion("07:05:45PM"))
    print(timeConversion("12:05:45PM"))
    print(timeConversion("12:05:45AM"))
    print(timeConversion("05:05:45AM"))

