'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def match(s, p):
            if not p:
                return not s

            m1 = s[0] == p[0] or p[0] == "."

            if len(p) >= 2 and p[1] == "*":
                return match(s, p[2:]) or m1 and match(s[1:], p[1:])
            else:
                return m1 and match(s[1:], p[1:])

        return match(s, p)


            # if s[0] == p[0]:
            #     return match(s[1:], p[1:])
            # elif p[0] == "*":
            #     return match(s[1:], p[1:])
            # elif p[0] == "." and p[1] == "*":
            #     return match(s, p[1:])





s = Solution()
print(s.isMatch("aab", "c*a*b"))
print(s.isMatch("aaab", ".*b"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("aaab", "aaab"))
print(s.isMatch("aa", "a"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("mississippi", "mis*is*p*."))