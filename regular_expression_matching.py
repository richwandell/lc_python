'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ss, ps = [], []

        si, pi = 0, 0
        cm = s[0]
        while len(ss) + len(ps) < len(s) + len(p):
            sc, pc = s[si], p[pi]

            if pc == ".":
                ps.append(".")
                if p[pi + 1] == "*":
                    ps.append("*")
                    pi += 2

                    while len(p) > pi:
                        pc = p[pi]
                        ps.append(pc)
                        pi += 1
                        if pc != "." and pc != "*":
                            endc = pc
                            while sc != endc:
                                ss.append(sc)
                                si += 1
                                sc = s[si]
                            ss.append(sc)
                            break
            elif pc == "*":
                mc = p[pi - 1]


                cm = ss[-1]




s = Solution()
print(s.isMatch("aaab", ".*b"))
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("aab", "c*a*b"))
print(s.isMatch("mississippi", "mis*is*p*."))