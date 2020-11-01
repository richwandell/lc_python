from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        if len(strs) == 0: return ""
        f = strs.pop()

        c = ""
        for i, l in enumerate(f):
            for j, str in enumerate(strs):
                if len(str) <= i:
                    return c
                if l != str[i]:
                    return c
            c += l

        return c

s = Solution()
assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
assert s.longestCommonPrefix(["","b"]) == ""
assert s.longestCommonPrefix(["aaa","aa","aaa"]) == "aa"