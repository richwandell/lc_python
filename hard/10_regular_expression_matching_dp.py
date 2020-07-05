'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matches = {}
        def match(i, j):
            if (i, j) not in matches:

                if j == len(p):
                m1 = s[0] == p[0] or p[0] == "."
                if len(p) >= 2 and p[1] == "*":
                    ret = match(s, p[2:]) or m1 and match(s[1:], p[1:])
                else:
                    ret = m1 and match(s[1:], p[1:])
                matches[s, p] = ret
            return matches[s, p]
        return match(0, 0)


s = Solution()
print(s.isMatch("aab", "c*a*b"))
print(s.isMatch("aaab", ".*b"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("aaab", "aaab"))
print(s.isMatch("aa", "a"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("mississippi", "mis*is*p*."))