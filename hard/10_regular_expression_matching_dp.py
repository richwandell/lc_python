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
                    ret = i == len(s)
                else:
                    m1 = i < len(s) and (s[i] == p[j] or p[j] == ".")

                    if j+1 < len(p) and p[j + 1] == "*":
                        ret = match(i, j+2) or (m1 and match(i+1, j))
                    else:
                        ret = m1 and match(i+1, j+1)
                matches[i, j] = ret
            else:
                print("in matches")
            return matches[i, j]
        return match(0, 0)


s = Solution()
print(s.isMatch("aab", "c*a*b"))
print(s.isMatch("aaab", ".*b"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("aaab", "aaab"))
print(s.isMatch("aa", "a"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("mississippi", "mis*is*p*."))