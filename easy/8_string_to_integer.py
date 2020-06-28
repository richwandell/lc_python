class Solution:
    def myAtoi(self, str: str) -> int:
        ns = str.strip()
        if ns == "":
            return 0
        rn = 0
        i = 0
        neg = False
        if ns[0] == "-":
            neg = True
            i += 1
        elif ns[0] == "+":
            neg = False
            i += 1

        def done():
            r = rn if not neg else -rn
            if r < -2147483648:
                return -2147483648
            elif r > 2147483647:
                return 2147483647
            return r

        while i < len(ns):
            c = ns[i]
            if 48 <= ord(c) <= 57:
                rn = rn * 10 + int(c)
                i += 1
            else:
                return done()

        return done()


s = Solution()
outs = [
    s.myAtoi("42"),
    s.myAtoi("   -42"),
    s.myAtoi("4193 with words"),
    s.myAtoi("words and 987"),
    s.myAtoi("-91283472332"),
]

print(outs)
