from typing import List


class Solution:
    """
    Write a function that reverses a string. The input string is given as an array of characters s.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
    """
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s)-1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

s = Solution()
# a = ["h","e","l","l","o"]
# s.reverseString(a)
# print(a)
# a = ["H","a","n","n","a","h"]
# s.reverseString(a)
# print(a)

a = ["h", "j"]
s.reverseString(a)
print(a)