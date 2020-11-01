class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0: return 0
        h, hl = 0, len(haystack)

        while h < hl:
            all = True
            for i, n in enumerate(needle):
                if h + i >= hl:
                    return -1
                if haystack[h + i] != n:
                    all = False
                    break
            if all:
                return h
            h += 1
        return -1

s = Solution()

assert s.strStr("hello", "ll") == 2
assert s.strStr("aaaaa", "bba") == -1
assert s.strStr("", "") == 0
assert s.strStr("aaa", "aaaa") == -1
