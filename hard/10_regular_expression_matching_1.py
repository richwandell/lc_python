class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def match(s, p):
            if not p:
                return s == ''

            # first character
            # true if first characters match
            # true if pattern first character is a dot
            m = bool(s) and (p[0] == s[0] or p[0] == ".")
            if len(p) >= 2 and p[1] == "*":
                return match(s, p[2:]) or (m and match(s[1:], p))
            else:
                return m and match(s[1:], p[1:])

        return match(s, p)

s = Solution()
print(s.isMatch("aab", "c*a*b")) # true
print(s.isMatch("aaab", ".*b"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("aaab", "aaab"))
print(s.isMatch("aa", "a"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("mississippi", "mis*is*p*."))