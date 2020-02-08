class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        def subst(start, string):
            if len(string) == start:
                return [0]

            current = set([])
            i = start
            while i < len(string):
                c = s[i]
                if c in current:
                    return [i - start] + subst(start+1, string)
                else:
                    current.add(c)
                i += 1
            return [i - start]

        strings = sorted(subst(0, s), reverse=True)
        return strings[0]


s = Solution()

print(s.lengthOfLongestSubstring("pwwkew"))