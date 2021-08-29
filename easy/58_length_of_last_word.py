class Solution:
    """
    Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
    """
    def lengthOfLastWord(self, s: str) -> int:
        l, i = 0, len(s)-1

        while i > -1:
            if l > 0 and s[i] == " ":
                break
            elif s[i] != " ":
                l += 1
            i -= 1
        return l

s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord("luffy is still joyboy"))